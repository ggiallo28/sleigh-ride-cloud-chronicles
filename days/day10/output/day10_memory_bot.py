# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import List, Dict

# -------------------------------------
# Day 10 – Rudy's Memory (Short Term)
# Minimal Starter Script (Session State)
# -------------------------------------

REGION = "us-east-1"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_CHAT = "../input/chat_history.json"
OUTPUT_FILE = "chat_session.log"

# TODO: Create Bedrock client
bedrock = None


def load_chat_history(path: str) -> List[Dict[str, str]]:
    """TODO: Load the simulated user chat messages from JSON."""
    pass


def format_messages_for_bedrock(history: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    TODO: Format the conversation history for the Bedrock Converse API.
    """
    pass


def chat_with_model(messages: List[Dict[str, Any]]) -> str:
    """
    TODO: Send the full conversation history to the model and get a response.
    
    Hint: Use the `bedrock.converse()` API for easier state management.
    """
    pass


def save_transcript(path: str, history: List[Dict[str, str]]):
    """TODO: Save the full conversation transcript to a text file."""
    pass


def main():
    # TODO: Implement the Chatbot Loop
    # 1. Load the input user messages.
    # 2. Initialize an empty conversation history list.
    # 3. Loop through each user message:
    #    a. Add user message to history.
    #    b. Call the model with the *entire* history.
    #    c. Get response and add assistant message to history.
    #    d. Print the turn.
    # 4. Save the final transcript.
    pass


if __name__ == "__main__":
    main()
