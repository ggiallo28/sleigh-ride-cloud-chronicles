# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import List, Dict, Any

# -------------------------------------
# Day 13 – Enter Rudy (The Orchestrator)
# Minimal Starter Script (Agent Persona)
# -------------------------------------

REGION = "us-east-1"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

# For Bedrock Agents (Option B)
AGENT_ID = None  # TODO: Set your Bedrock Agent ID if using Option B
AGENT_ALIAS_ID = None  # TODO: Set your Agent Alias ID if using Option B

INPUT_PERSONA = "../input/rudy_persona.txt"
OUTPUT_FILE = "rudy_response.txt"

# TODO: Create Bedrock clients
bedrock_runtime = None  # For Option A (direct LLM)
bedrock_agent_runtime = None  # For Option B (Bedrock Agent)


def load_persona(path: str) -> str:
    """TODO: Load the persona definition from text file."""
    pass


def build_system_prompt(persona: str) -> str:
    """
    TODO: Build a system prompt that enforces Rudy's personality.
    
    The system prompt should:
    1. Define who Rudy is (name, role)
    2. Establish his personality traits
    3. Set his goals and constraints
    4. Encourage in-character responses
    
    """
    pass



# OPTION A: Simulated Agent Loop (Direct LLM)

def chat_with_rudy_llm(system_prompt: str, user_message: str) -> str:
    """
    TODO: Send a message to Rudy using direct LLM invocation.
    
    This simulates an agent by using a system prompt with the Converse API.
    Good for quick testing without setting up a full Bedrock Agent.
    
    Hint: Use bedrock_runtime.converse() with:
    - modelId
    - system parameter for the persona
    - messages list with the user message
    """
    pass



# OPTION B: Amazon Bedrock Agent

def chat_with_rudy_agent(user_message: str, session_id: str = "rudy-session") -> str:
    """
    TODO: Send a message to Rudy using a configured Bedrock Agent.
    
    Prerequisites:
    1. Create a Bedrock Agent in the AWS Console
    2. Configure the agent with the system prompt
    3. Create an alias and set AGENT_ID and AGENT_ALIAS_ID above
    
    Hint: Use bedrock_agent_runtime.invoke_agent() with:
    - agentId
    - agentAliasId
    - sessionId (for conversation continuity)
    - inputText
    """
    pass


def save_transcript(path: str, user_message: str, rudy_response: str):
    """TODO: Save the conversation transcript to a text file."""
    pass


def main():
    # TODO: Implement the Rudy Agent interaction
    # 
    # Choose your approach:
    #
    # OPTION A - Simulated Agent (Quick Start):
    # 1. Load the persona definition from input file
    # 2. Build a system prompt incorporating the persona
    # 3. Use chat_with_rudy_llm() to interact
    #
    # OPTION B - Bedrock Agent (Full Agent Experience):
    # 1. First, create a Bedrock Agent in AWS Console with the persona
    # 2. Set AGENT_ID and AGENT_ALIAS_ID at the top of this file
    # 3. Use chat_with_rudy_agent() to interact
    #
    # Common steps:
    # 4. Define a test message (e.g., "How is the schedule looking?")
    # 5. Print Rudy's response
    # 6. Save the transcript to output file
    pass


if __name__ == "__main__":
    main()
