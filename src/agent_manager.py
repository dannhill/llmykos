from __future__ import annotations
import random
import threading
import logging
from typing import Optional

from src import users, channels, history
from src.agent import Agent, PERSONALITIES
from src.dispatcher import MessageDispatcher
from src.gamejoin import join_player
from src.status import add_dying, kill_players
from src.users import User, FakeUser

class AgentManager:
    def __init__(self):
        logging.debug("Initializing AgentManager")
        self.agents: list[Agent] = []
        self._nick_counter = 0
        self._speaking_timer: Optional[threading.Timer] = None
        self._voting_timer: Optional[threading.Timer] = None
        self.name_list : list[str] = ["jason", "alice", "bob", "jack", "michael", "sarah", "david", "laura", "chris", "emma"]

    def clear_agents(self):
        """Removes all AI agents from the game."""
        for agent in list(self.agents):
            self.remove_agent(agent.user)

    def create_agent(self, personality: Optional[str] = None) -> Optional[Agent]:
        """Creates a new AI agent."""
        if not PERSONALITIES:
            return None

        if personality is None:
            personality = random.choice(list(PERSONALITIES.keys()))
        elif personality not in PERSONALITIES:
            return None

        # Keep trying to find a nick that is not in use
        while True:
            self._nick_counter += 1
            nick = str(self._nick_counter)  # self.name_list[self._nick_counter % len(self.name_list)] not working cause of hashin problems #TODO
            if users.get(nick, allow_none=True) is None:
                break

        # The first argument to add is the client, which is None for fake users.
        user = users.add(None, nick=nick, ident="AI", host="wolf.game", account=nick)

        if not isinstance(user, FakeUser):
            users._users.discard(user)
            return None

        agent = Agent(user, personality)
        self.agents.append(agent)
        return agent

    def join_agent_to_game(self, agent: Agent):
        """Joins an AI agent to the game."""
        channels.Main.users.add(agent.user)
        agent.user.channels[channels.Main] = set()

        join_wrapper = MessageDispatcher(agent.user, channels.Main)
        join_player(join_wrapper)

    def remove_agent(self, user: User) -> bool:
        """Removes an AI agent from the game."""
        agent_to_remove = self.get_agent(user)

        if agent_to_remove:
            self.agents.remove(agent_to_remove)

            if channels.Main.game_state and user in channels.Main.game_state.players:
                add_dying(channels.Main.game_state, user, "bot", "remove", death_triggers=False)
                kill_players(channels.Main.game_state)

            users._users.discard(user)
            return True

        return False

    def get_agent(self, user: User) -> Optional[Agent]:
        """Gets the agent associated with a user."""
        for agent in self.agents:
            if agent.user is user:
                return agent
        return None

    def start_speaking(self):
        """Starts the agent speaking timer."""
        if self._speaking_timer is None:
            print(f"Starting speaking timer SCHEDULER for agents.")
            self._schedule_speaking()
        if self._voting_timer is None:
            self._schedule_voting()

    def stop_speaking(self):
        """Stops the agent speaking timer."""
        if self._speaking_timer:
            self._speaking_timer.cancel()
            self._speaking_timer = None
        if self._voting_timer:
            self._voting_timer.cancel()
            self._voting_timer = None

    def stop_voting(self):
        """Stops the agent voting timer."""
        if self._voting_timer:
            self._voting_timer.cancel()
            self._voting_timer = None
        

    def _schedule_voting(self):
        """Schedules the next voting event."""
        if not channels.Main.game_state or channels.Main.game_state.current_phase != "day":
            self.stop_voting()
            return

        interval = random.uniform(10, 20)
        self._voting_timer = threading.Timer(interval, self._voting_tick)
        self._voting_timer.daemon = True
        self._voting_timer.start()

    def _voting_tick(self):
        """Called by the timer to make an agent vote."""
        print(f"Agent voting tick.")
        if not self.agents:
            self.stop_voting()
            return

        if self.agents:
            voting_chance = 1 / len(self.agents)
            for agent in self.agents:
                if random.random() < voting_chance:
                    agent.generate_vote()
                    break

        self._schedule_voting()

    def _schedule_speaking(self):
        """Schedules the next speaking event."""
        if not channels.Main.game_state or channels.Main.game_state.current_phase != "day":
            print(f"Stopping speaking timer for agents cause game is not in day phase or game is not active.")
            self.stop_speaking()
            return

        # num of players * 5
        average_interval = int(len(channels.Main.game_state.players) * 5)
        interval = random.uniform(average_interval - 3, average_interval + 3)
        self._speaking_timer = threading.Timer(interval, self._speaking_tick)
        self._speaking_timer.daemon = True
        self._speaking_timer.start()
        print(f"Started speaking timer for agents.")

    def _speaking_tick(self):
        """Called by the timer to make an agent speak."""
        print(f"Agent speaking tick.")
        if not self.agents:
            self.stop_speaking()
            return

        if self.agents:
            speaking_chance = 1 / len(channels.Main.game_state.players)
            for agent in self.agents:
                if random.random() < speaking_chance:
                    context = history.get_history()
                    response = agent.generate_response(context)
                    if response:
                        logging.info(f"Agent {agent.user.nick} says: {response}")
                        channels.Main.send(f"<{agent.user.nick}> {response}")
                    break

        self._schedule_speaking()

# Singleton instance
agent_manager = AgentManager()
