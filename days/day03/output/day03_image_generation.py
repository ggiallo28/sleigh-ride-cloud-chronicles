import boto3
import json
import base64

# -------------------------------------
# Day 3 – Image Generation
# Minimal Starter Skeleton (Same Style as Day 1 & 2)
# -------------------------------------

REGION = "us-east-1"
IMAGE_MODEL_ID = "amazon.nova-canvas-v1:0"

INPUT_FILE = "letter_002.txt"
OUTPUT_FILE = "card_cover.png"

bedrock = boto3.client("bedrock-runtime", region_name=REGION)


def load_letter(path):
    """TODO: Load the letter text."""
    pass


def build_prompt(letter_text):
    """TODO: Build the IMAGE GENERATION prompt."""
    pass


def call_image_model(prompt):
    """TODO: Call Bedrock image model and return PNG bytes."""
    pass


def save_image(path, image_bytes):
    """TODO: Save generated PNG to file."""
    pass


def main():
    # TODO: Implement steps:
    # 1. Load letter
    # 2. Build image prompt
    # 3. Call image model
    # 4. Save PNG
    pass


if __name__ == "__main__":
    main()
