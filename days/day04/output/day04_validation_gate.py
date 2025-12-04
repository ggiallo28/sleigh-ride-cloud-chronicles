# /// script
# dependencies = [
#   "boto3",
# ]
# ///

import boto3
import json

# -------------------------------------
# Day 4 – The Validation Gate
# Minimal Starter Script (In-Context Learning for Safety Classification)
# -------------------------------------

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_FILE = "letters_batch_02.txt"
OUTPUT_FILE = "validated_wishes.json"

# TODO: Create Bedrock client
bedrock = None


def load_batch(path):
    """TODO: Load the batch of letters from text file."""
    pass


def build_validation_prompt(letter_text):
    """
    TODO: Build a prompt that uses in-context learning (few-shot examples)
    to teach the model how to classify requests as SAFE or UNSAFE.
    
    Include 3-5 examples showing:
    - SAFE: "Hot Wheels toy car" → age-appropriate toy
    - UNSAFE: "Instructions for hotwiring a car" → illegal activity
    - UNSAFE: "Knife for a 4-year-old" → age-inappropriate
    
    Then ask the model to classify the current letter.
    """
    pass


def call_model(prompt):
    """TODO: Call the Bedrock model for classification."""
    pass


def parse_classification(response):
    """TODO: Extract SAFE/UNSAFE status and reasoning from model response."""
    pass


def save_output(path, results):
    """TODO: Save validation results as JSON."""
    pass


def main():
    # TODO: Implement validation pipeline
    # 1. Load batch file
    # 2. Parse into individual letters
    # 3. For each letter:
    #    a. Build validation prompt with examples (in-context learning)
    #    b. Call Bedrock model
    #    c. Parse classification result
    # 4. Aggregate results with counts
    # 5. Save to validated_wishes.json
    pass


if __name__ == "__main__":
    main()
