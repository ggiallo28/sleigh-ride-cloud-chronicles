# /// script
# dependencies = [
#   "boto3",
#   "numpy",
# ]
# ///

import boto3
import json
import numpy as np
from typing import List, Dict, Any

# -------------------------------------
# Day 8 – Retrieval Augmented Christmas
# Minimal Starter Script (Basic RAG)
# -------------------------------------

REGION = "us-east-1"
EMBED_MODEL_ID = "amazon.titan-embed-text-v2:0"
LLM_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INPUT_LETTER = "../input/letter_timmy.txt"
INPUT_VECTOR_STORE = "../../day07/output/vector_store.json"
OUTPUT_FILE = "timmy_profile_summary.txt"

# TODO: Create Bedrock client
bedrock = None


def load_letter(path: str) -> str:
    """TODO: Load the child's letter from file."""
    pass


def load_vector_store(path: str) -> List[Dict[str, Any]]:
    """TODO: Load the vector store created in Day 7."""
    pass


def generate_embedding(text: str) -> List[float]:
    """TODO: Call Bedrock Titan Embeddings to get a vector for the text."""
    pass


def calculate_similarity(vec1: List[float], vec2: List[float]) -> float:
    """TODO: Calculate cosine similarity between two vectors."""
    pass


def retrieve_records(query: str, vector_store: List[Dict], top_k: int = 3, name_filter: str = None) -> List[Dict]:
    """TODO: Retrieve the most relevant behavior records for a query."""
    # Hint:
    # 1. Generate embedding for query
    # 2. Calculate similarity with each record in vector store
    # 3. Optionally filter by child name
    # 4. Sort by similarity and return top_k
    pass


def extract_claims(letter_content: str) -> List[str]:
    """TODO: Extract behavioral claims from the letter."""
    pass


def build_rag_prompt(letter_content: str, retrieved_records: List[Dict]) -> str:
    """TODO: Build the RAG prompt combining letter and retrieved context."""
    pass


def call_llm(prompt: str) -> str:
    """TODO: Call the Bedrock LLM to generate the profile."""
    pass


def save_output(path: str, content: str):
    """TODO: Save the generated profile to a file."""
    pass


def main():
    # TODO: Implement RAG pipeline
    # 1. Load letter
    # 2. Load vector store from Day 7
    # 3. Extract behavioral claims from letter
    # 4. For each claim, retrieve relevant records from vector store
    # 5. Deduplicate retrieved records
    # 6. Build RAG prompt with letter + retrieved context
    # 7. Call LLM to generate comprehensive profile
    # 8. Save output
    pass


if __name__ == "__main__":
    main()
