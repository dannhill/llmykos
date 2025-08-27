import os
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
        self.system_prompt = PERSONALITIES[personality]

        if GEMINI_MODEL_NAME:
            self._client = genai.GenerativeModel(GEMINI_MODEL_NAME, system_instruction=self.system_prompt)
        else:
            self._client = None

    def generate_response(self, context: str) -> str:
        """
        Generates a response based on the given context.
        """
        if not self._client:
            return "" # Or some default response

        # This is a placeholder for the actual implementation
        # of how the agent will generate a response.
        # It will involve calling the Gemini API with the context.
        response = self._client.generate_content(context)
        return response.text
