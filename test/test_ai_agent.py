#test the ai agent inference via llm using the .env file GEMINI_API_KEY and GEMINI_MODEL_NAME
from unittest import TestCase
import os
import logging
from src.agent import Agent
from src.agent_manager import AgentManager

class TestAIAgent(TestCase):
    def test_agent_inference(self):
        self.agent_manager = AgentManager()
        agent = self.agent_manager.create_agent()
        assert agent is not None
        response = agent.generate_response("Hello, how are you?")
        #log inside a file newly opened
        with open("test_agent_inference.log", "a") as f:
            f.write(f"Agent response: {response}\n")
        assert response is not None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ai_agent_test = TestAIAgent()
    ai_agent_test.test_agent_inference()