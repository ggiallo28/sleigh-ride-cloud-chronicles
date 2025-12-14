# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json
from typing import List, Dict, Any

# -------------------------------------
# Day 12 – The Priority Queue
# Minimal Starter Script (Qualitative Ranking)
# -------------------------------------

REGION = "us-east-1"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_REQUESTS = "../input/gift_requests.json"
OUTPUT_FILE = "prioritized_list.json"

# Priority Rubric
PRIORITY_RUBRIC = """
5: Critical (Health, Safety, Crisis)
4: High (Emotional Distress, Basic Needs, Animal Welfare)
3: Standard (Normal Wishes)
2: Low (Minor wants, replacements)
1: Trivial (Greed, impossible items)
"""

# TODO: Create Bedrock client
bedrock = None


def load_requests(path: str) -> List[Dict[str, Any]]:
    """TODO: Load the gift requests from JSON file."""
    pass


def build_scoring_prompt(request: Dict[str, Any]) -> str:
    """
    TODO: Build a prompt to score a single request.
    
    The prompt should:
    1. Include the priority rubric
    2. Present the child's request and context
    3. Ask for a JSON response with 'score' and 'reason'
    
    Hint: Be explicit about the output format you expect.
    """
    pass


def call_llm(prompt: str) -> str:
    """
    TODO: Call the Bedrock LLM to get the priority score.
    
    Hint: Use bedrock.invoke_model() with the appropriate payload.
    """
    pass


def parse_score_response(response: str) -> Dict[str, Any]:
    """
    TODO: Parse the LLM response to extract score and reasoning.
    
    Expected output format:
    {
        "score": 5,
        "reason": "Medical context and high emotional need."
    }
    """
    pass


def score_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Score a single request and return enriched data.
    
    Returns the original request data plus:
    - priority_score
    - reasoning
    """
    pass


def sort_by_priority(requests: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    TODO: Sort requests by priority score in descending order.
    
    Hint: Use sorted() with a key function.
    """
    pass


def save_prioritized_list(path: str, requests: List[Dict[str, Any]]):
    """TODO: Save the prioritized list to a JSON file."""
    pass


def main():
    # TODO: Implement the Priority Queue pipeline
    # 1. Load the gift requests from input file
    # 2. Loop through each request:
    #    a. Build a scoring prompt with the rubric
    #    b. Call the LLM to get priority score
    #    c. Parse the response and enrich the request data
    # 3. Sort all requests by priority (descending)
    # 4. Save the prioritized list to output file
    pass


if __name__ == "__main__":
    main()
