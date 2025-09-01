import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from src.users import FakeUser

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

PERSONALITIES = {
    "cautious": "You are a werewolf player. You must be cautious in your actions. If you are a wolf, you don't have to accuse people randomly, but you have to stay behind.",
    "aggressive": "You are a werewolf player. You must be aggressive in your actions. You are not afraid to accuse others, even with little evidence.",
    "quiet": "You are a werewolf player. You are very quiet and don't talk much. You prefer to observe and analyze the game silently.",
    "leader": "You are a werewolf player. You are a natural leader. You try to guide the village and organize the votes against suspected werewolves.",
}

class Agent:
    def __init__(self, user: FakeUser, personality: str):
        if personality not in PERSONALITIES:
            raise ValueError(f"Unknown personality: {personality}")

        self.user = user
        self.personality = personality
        self.writing_style = "You don't have to think about your responses out loud, you just have to respond naturally knowing that everyone is listening. Use an informal writing style and don't write too long sentences. In addition you should never go next line, write everything in a single line."
        self.system_prompt = self.writing_style + "\n\n" + PERSONALITIES[personality]

        if GEMINI_MODEL_NAME:
            self._client = genai.GenerativeModel(GEMINI_MODEL_NAME, system_instruction=self.system_prompt)
        else:
            self._client = None

    def generate_response(self, context: str) -> str:
        """
        Generates a response based on the given context.
        """
        if not self._client:
            return ""

        messages = context.strip().split('\n')
        contents = []
        for msg in messages:
            match = re.match(r'<([^>]+)> (.*)', msg)
            if match:
                author, text = match.groups()
                role = "model" if author == self.user.nick else "user"
                contents.append({
                    "role": role,
                    "parts": [{"text": f"{author}: {text}"}]
                })
            else:
                contents.append({
                    "role": "user",
                    "parts": [{"text": msg}]
                })

        response = self._client.generate_content(contents)
        return response.text

    def generate_vote(self):
        """
        Generates a vote for a player.
        """
        if not self._client:
            return

        from src.functions import get_players
        from src.gamestate import GameState
        from src.votes import VOTES
        from src.dispatcher import MessageDispatcher
        from src.handler import parse_and_dispatch
        from src import channels, history

        var = self.user.game_state
        if not var or not isinstance(var, GameState):
            return

        if self.user in VOTES:
            return

        players = get_players(var)
        if self.user in players:
            players.remove(self.user)

        if not players:
            return

        context = history.get_history()
        messages = context.strip().split('\n')
        contents = []
        for msg in messages:
            match = re.match(r'<([^>]+)> (.*)', msg)
            if match:
                author, text = match.groups()
                role = "model" if author == self.user.nick else "user"
                contents.append({
                    "role": role,
                    "parts": [{"text": f"{author}: {text}"}]
                })
            else:
                contents.append({
                    "role": "user",
                    "parts": [{"text": msg}]
                })

        player_names = [p.nick for p in players]
        prompt = f"Based on the conversation, who should you vote for? Please choose one of the following players: {', '.join(player_names)}. Only return the player's name. Write None to skip voting."
        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        response = self._client.generate_content(contents)
        player_to_vote = response.text.strip()

        if player_to_vote in player_names:
            wrapper = MessageDispatcher(self.user, channels.Main)
            parse_and_dispatch(wrapper, "vote", player_to_vote)