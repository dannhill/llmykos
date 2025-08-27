from __future__ import annotations
from collections import deque
from typing import Deque, Tuple
from datetime import datetime

from src.users import User

# Keep a history of the last 100 messages
CHAT_HISTORY: Deque[Tuple[datetime, str, str]] = deque(maxlen=100)

def add_message(user: User, message: str):
    """Adds a message to the chat history."""
    CHAT_HISTORY.append((datetime.now(), user.nick, message))

def get_history() -> str:
    """Returns the chat history as a formatted string."""
    return "\n".join(f"{nick}: {message}" for _, nick, message in CHAT_HISTORY)

def clear_history():
    """Clears the chat history."""
    CHAT_HISTORY.clear()
