from __future__ import annotations
import random
import threading
from typing import Optional

from src import users, wolfgame, channels, history
from src.agent import Agent, PERSONALITIES
from src.users import User, FakeUser
from src.context import NotLoggedIn

class AgentManager:
    def __init__(self):
        self.agents: list[Agent] = []
        self._nick_counter = 0
        self._speaking_timer: Optional[threading.Timer] = None

    def clear_agents(self):
        """Removes all AI agents from the game."""
        for agent in list(self.agents):
            self.remove_agent(agent.user)

    def create_agent(self, personality: Optional[str] = None) -> Optional[Agent]:
        """Creates a new AI agent and adds it to the game."""
        if not PERSONALITIES:
            return None

        if personality is None:
            personality = random.choice(list(PERSONALITIES.keys()))
        elif personality not in PERSONALITIES:
            return None

        # Keep trying to find a nick that is not in use
        while True:
            self._nick_counter += 1
            nick = str(self._nick_counter)
            if users.get(nick, allow_none=True) is None:
                break

        # The first argument to add is the client, which is None for fake users.
        user = users.add(None, nick=nick, ident="AI", host="wolf.game", account=NotLoggedIn)

        if not isinstance(user, FakeUser):
            # This shouldn't happen with a numeric nick, but as a safeguard:
            users._users.discard(user)
            return None

        agent = Agent(user, personality)
        self.agents.append(agent)
        return agent

    def remove_agent(self, user: User) -> bool:
        """Removes an AI agent from the game."""
        from src import wolfgame

        agent_to_remove = self.get_agent(user)

        if agent_to_remove:
            self.agents.remove(agent_to_remove)

            if wolfgame.GAME_STATE and user in wolfgame.GAME_STATE.players:
                wolfgame.del_participant(wolfgame.GAME_STATE, user)

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
            self._schedule_speaking()

    def stop_speaking(self):
        """Stops the agent speaking timer."""
        if self._speaking_timer:
            self._speaking_timer.cancel()
            self._speaking_timer = None

    def _schedule_speaking(self):
        """Schedules the next speaking event."""
        if not wolfgame.GAME_STATE or wolfgame.GAME_STATE.current_phase != "day":
            self.stop_speaking()
            return

        interval = random.uniform(7, 13)
        self._speaking_timer = threading.Timer(interval, self._speaking_tick)
        self._speaking_timer.daemon = True
        self._speaking_timer.start()

    def _speaking_tick(self):
        """Called by the timer to make an agent speak."""
        if not self.agents:
            self.stop_speaking()
            return

        # Each agent has a 1/n chance of speaking
        if self.agents:
            speaking_chance = 1 / len(self.agents)
            for agent in self.agents:
                if random.random() < speaking_chance:
                    context = history.get_history()
                    response = agent.generate_response(context)
                    if response:
                        channels.Main.send(f"<{agent.user.nick}> {response}")
                    break # Only one agent speaks per tick

        self._schedule_speaking()

# Singleton instance
agent_manager = AgentManager()
