# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import List, Dict, Any

# -------------------------------------
# Day 15 – Agent Collaboration
# Rudy (Orchestrator) + Elfie (Tool User)
# -------------------------------------

REGION = "us-east-1"

# Rudy uses a smarter model for planning
RUDY_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
# Elfie can use a faster/cheaper model for tool calls
ELFIE_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

INPUT_WISH = "../input/complex_wish.txt"
OUTPUT_LOG = "collaboration_log.txt"

# TODO: Create Bedrock client
bedrock_runtime = None


# ============================================
# RUDY - The Orchestrator
# ============================================

def load_wish(path: str) -> str:
    """TODO: Load the complex wish from text file."""
    pass


def build_rudy_system_prompt() -> str:
    """
    TODO: Build Rudy's system prompt for task decomposition.
    
    The prompt should:
    1. Define Rudy as the anxious, dramatic Orchestrator
    2. Instruct him to analyze wishes and identify ALL items
    3. Request JSON output format: {"analysis": "...", "items": ["item1", "item2"]}
    """
    pass


def ask_rudy_to_plan(wish_text: str) -> Dict[str, Any]:
    """
    TODO: Ask Rudy to analyze the wish and output a structured plan.
    
    Hint: Use bedrock_runtime.converse() with:
    - modelId: RUDY_MODEL_ID
    - system: Rudy's planning prompt
    - messages: The wish text
    
    Returns a dict with 'analysis' and 'items' list.
    """
    pass


# ============================================
# ELFIE - The Tool User
# ============================================

def build_elfie_system_prompt() -> str:
    """
    TODO: Build Elfie's system prompt for tool calling.
    
    The prompt should:
    1. Define Elfie as the cheerful Tool User
    2. Describe the get_inventory tool (name, description, parameters)
    3. Request JSON tool call output format
    
    Reuse the tool schema from Day 14 (define_tool_schema).
    """
    pass


def ask_elfie_for_tool_call(item_name: str) -> Dict[str, Any]:
    """
    TODO: Ask Elfie to generate a tool call for checking inventory.
    
    Hint: Use bedrock_runtime.converse() with:
    - modelId: ELFIE_MODEL_ID
    - system: Elfie's tool prompt
    - messages: Simple task like "Check inventory for: {item_name}"
    
    Returns the tool call JSON structure.
    """
    pass


# ============================================
# COLLABORATION ORCHESTRATION
# ============================================

def run_collaboration(wish_text: str) -> List[str]:
    """
    TODO: Orchestrate the collaboration between Rudy and Elfie.
    
    Flow:
    1. Ask Rudy to analyze the wish and get list of items
    2. For each item in Rudy's plan:
       - Pass the item to Elfie
       - Capture Elfie's tool call
    3. Build a log of the interaction
    
    Returns a list of log entries.
    """
    pass


def save_log(path: str, log_entries: List[str]):
    """TODO: Save the collaboration log to a text file."""
    pass


def main():
    # TODO: Implement the Agent Collaboration
    #
    # 1. Load the complex wish from input file
    # 2. Run the collaboration:
    #    - Rudy analyzes and breaks down the wish into tasks
    #    - For each task, Elfie generates the appropriate tool call
    # 3. Print and save the collaboration log
    #
    # Expected log format:
    #   Rudy: Analyzing wish... Identified X items.
    #   Rudy: Task 1 -> Check Red Racing Bike.
    #   Elfie: Tool Call -> get_inventory("Red Racing Bike")
    #   ...
    pass


if __name__ == "__main__":
    main()
