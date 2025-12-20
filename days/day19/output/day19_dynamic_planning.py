# /// script
# dependencies = [
#   "boto3",
#   "strands-agents",
# ]
# ///

import json
import boto3
from typing import Dict, Any

# -------------------------------------
# Day 19 – Dynamic Planning
# Rudy reasons about situations and creates adaptive plans
# -------------------------------------

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_GOALS = "../input/planning_goals.txt"

# TODO: Create Bedrock client
bedrock_runtime = None


# ============================================
# PLANNING FUNCTIONS
# ============================================


def load_goals(path: str) -> str:
    """TODO: Load planning goals from text file."""
    pass


def load_scenario(path: str) -> Dict[str, Any]:
    """TODO: Load scenario from JSON file."""
    pass


def build_planning_prompt(goals: str, scenario: Dict[str, Any]) -> str:
    """
    TODO: Build a prompt for Rudy to create a dynamic plan.

    The prompt should:
    1. Establish Rudy's role as a reasoning agent (not a script follower)
    2. Include the planning goals and constraints
    3. Provide the current scenario context
    4. Ask Rudy to analyze the situation
    5. Request a JSON plan with:
       - situation_analysis
       - goal
       - plan (action, reasoning, confidence, requires_approval, next_agent)

    Example structure:
    '''
    You are Rudy, the Planning Agent for Project Sleigh-Ride.
    You do NOT follow fixed pipelines. You REASON about each situation.

    PLANNING GOALS AND CONSTRAINTS:
    {goals}

    CURRENT SITUATION:
    Child: {child_name}
    Wish: {extracted_wish}
    Budget: ${budget}
    Behavior Score: {behavior_score}
    Current State: {current_state}

    TASK:
    Analyze this situation and create a dynamic plan.
    - What's the current state?
    - What constraints apply?
    - What's the best next action?
    - Why is this the right choice?
    - How confident are you?

    Output ONLY valid JSON in this format:
    {
      "situation_analysis": "...",
      "goal": "...",
      "plan": {
        "action": "...",
        "reasoning": "...",
        "confidence": 0.0-1.0,
        "requires_approval": true/false,
        "next_agent": "..."
      }
    }
    '''
    """
    pass


def ask_rudy_to_plan(prompt: str) -> Dict[str, Any]:
    """
    TODO: Send planning prompt to Rudy and get dynamic plan.

    Steps:
    1. Use bedrock_runtime.converse() with:
       - modelId: MODEL_ID
       - messages: [{"role": "user", "content": [{"text": prompt}]}]
    2. Extract the response text
    3. Parse the JSON response
    4. Return the plan dict

    Hint: The response will be in:
    response['output']['message']['content'][0]['text']
    """
    pass


def save_plan(path: str, plan: Dict[str, Any]):
    """TODO: Save the plan to a JSON file."""
    pass


def print_plan_summary(scenario_name: str, plan: Dict[str, Any]):
    """
    TODO: Print a human-readable summary of the plan.

    Example output:
    SCENARIO: Simple
    ANALYSIS: Item found in inventory, all constraints satisfied
    GOAL: Fulfill wish
    ACTION: approve_order
    NEXT: elfie
    """
    pass


# ============================================
# MAIN ORCHESTRATION
# ============================================


def main():
    """
    TODO: Demonstrate dynamic planning with both scenarios.

    Flow:
    1. Load planning goals (same for both scenarios)
    2. Test Scenarios:
       - Load scenario (create examples)
       - Build planning prompt
       - Ask Rudy to plan
       - Save and display plan
    3. Compare the plans to show Rudy adapts to context

    Expected outcome:
    - Simple scenarios: Direct approval
    - Complex scenarios: Alternative suggestion, requires approval
    - Demonstrates that Rudy reasons differently based on situation
    """


if __name__ == "__main__":
    main()
