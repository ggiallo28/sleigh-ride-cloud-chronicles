# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import Dict, Any, Optional

# -------------------------------------
# Day 14 – Enter Elfie (The Tool User)
# Minimal Starter Script (Tool Definition & Function Call Output)
# -------------------------------------

REGION = "us-east-1"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

OUTPUT_FILE = "tool_call.json"

# TODO: Create Bedrock client
bedrock = None


def define_tool_schema() -> str:
    """
    TODO: Define the tool schema as a string to include in the prompt.
    
    Describe the get_inventory function:
    - Name: get_inventory
    - Description: What it does
    - Parameters: item_name (string, required)
    
    Return a string that explains the tool to the model.
    """
    pass


def build_elfie_prompt(tool_schema: str, user_question: str) -> str:
    """
    TODO: Build the full prompt for Elfie.
    
    The prompt should:
    1. Define Elfie's persona (cheerful, efficient, uses tools)
    2. Include the tool schema
    3. Instruct the model to output a JSON function call (not answer directly)
    4. Include the user's question
    
    Example output format to request:
    {
        "tool_name": "get_inventory",
        "parameters": {
            "item_name": "..."
        }
    }
    """
    pass


def call_llm(prompt: str) -> str:
    """TODO: Call the Bedrock LLM and return the response text."""
    pass



def main():
    # TODO: Implement the Tool Call Test
    # 1. Define the tool schema
    # 2. Build the prompt with a test question: "How many Red Racing Bikes do we have?"
    # 3. Call the LLM
    # 4. Read the tool call JSON from the response
    # 5. Verify the output has correct tool_name and parameters
    pass


if __name__ == "__main__":
    main()
