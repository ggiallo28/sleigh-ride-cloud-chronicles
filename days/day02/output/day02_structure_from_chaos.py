# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json

# -------------------------------------
# Day 2 – Structure from Chaos
# Minimal Starter Script (Same Style as Day 1)
# -------------------------------------

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_FILE = "letters_batch_01.txt"
OUTPUT_FILE = "extracted_letters.json"

# TODO: Create Bedrock client
bedrock = None


def load_batch(path):
    """TODO: Load the batch of cleaned letters."""
    pass


def build_prompt(batch_text):
    """TODO: Build the entity extraction + JSON formatting prompt."""
    pass


def call_model(prompt):
    """TODO: Call the Bedrock model for structured extraction."""
    pass


def save_output(path, content):
    """TODO: Save extracted JSON to a file."""
    pass


def main():
    # TODO: Implement processing steps
    # 1. Load batch file
    # 2. Build extraction prompt
    # 3. Call Bedrock model
    # 4. Save structured JSON output
    pass


if __name__ == "__main__":
    main()
