# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import List, Dict, Any

# -------------------------------------
# Day 11 – The Moral Compass
# Minimal Starter Script (Chain-of-Thought)
# -------------------------------------

REGION = "us-east-1"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_SCENARIOS = "../input/ambiguous_scenarios.json"
OUTPUT_FILE = "moral_verdicts.json"

# TODO: Create Bedrock client
bedrock = None


def load_scenarios(path: str) -> List[Dict[str, Any]]:
    """TODO: Load the ambiguous scenarios from JSON file."""
    pass


def build_cot_prompt(scenario: Dict[str, Any]) -> str:
    """
    TODO: Build a Chain-of-Thought prompt for moral evaluation.

    The prompt should instruct the model to:
    1. Analyze the action (what happened)
    2. Analyze the intent (why it happened)
    3. Evaluate the outcome (harm vs good)
    4. Provide a final verdict

    Hint: Use "Let's think step by step" or explicit numbered steps.
    """
    pass


def call_llm(prompt: str) -> str:
    """
    TODO: Call the Bedrock LLM to get the moral evaluation.

    Hint: Use bedrock.invoke_model() with the appropriate payload.
    """
    pass


def parse_verdict(response: str) -> Dict[str, str]:
    """
    TODO: Parse the LLM response to extract reasoning and verdict.

    Expected output format:
    {
        "reasoning": "Step-by-step analysis...",
        "verdict": "NICE/NAUGHTY/COMPLEX"
    }
    """
    pass


def evaluate_scenario(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Evaluate a single scenario using Chain-of-Thought.

    Returns a dict with child_name, reasoning, and verdict.
    """
    pass


def save_verdicts(path: str, verdicts: List[Dict[str, Any]]):
    """TODO: Save the moral verdicts to a JSON file."""
    pass


def main():
    # TODO: Implement the Moral Compass pipeline
    # 1. Load the ambiguous scenarios from input file
    # 2. Initialize an empty list for verdicts
    # 3. Loop through each scenario:
    #    a. Build a CoT prompt for the scenario
    #    b. Call the LLM with the prompt
    #    c. Parse the response to extract reasoning and verdict
    #    d. Append result to verdicts list
    # 4. Save all verdicts to output file
    pass


if __name__ == "__main__":
    main()
