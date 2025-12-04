# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json

# ------------------------------
# Day 1 – The First Digital Letter
# Minimal Starter Script
# ------------------------------

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_FILE = "letter_001.txt"
OUTPUT_FILE = "letter_001_clean.md"

# TODO: Create Bedrock client
bedrock = None

def load_letter(path):
    """TODO: Load raw letter text."""
    pass

def build_prompt(raw_text):
    """TODO: Build your prompt here."""
    pass

def call_model(prompt):
    """TODO: Call the Bedrock model."""
    pass

def save_output(path, content):
    """TODO: Save the cleaned summary to a Markdown file."""
    pass

def main():
    # TODO: Implement processing steps
    # 1. Load letter
    # 2. Build prompt
    # 3. Call model
    # 4. Save cleaned summary
    pass

if __name__ == "__main__":
    main()