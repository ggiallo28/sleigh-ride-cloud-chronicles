# /// script
# dependencies = [
#   "boto3",
#   "numpy",
# ]
# ///

import boto3
import json
import csv
import numpy as np
from typing import List, Dict

# -------------------------------------
# Day 6 – The Vague Wish
# Minimal Starter Script (Semantic Search with Embeddings)
# -------------------------------------

REGION = "us-east-1"
MODEL_ID = "amazon.titan-embed-text-v2:0"

INPUT_CATALOG = "../input/toy_catalog.csv"
OUTPUT_FILE = "semantic_matches.json"

VAGUE_WISHES = [
    "something red that goes fast",
    "a toy for building things",
    "something cuddly and soft",
    "a game to play with my family"
]

# TODO: Create Bedrock client
bedrock = None


def load_catalog(path: str) -> List[Dict]:
    """TODO: Load the toy catalog from CSV."""
    pass


def generate_embedding(text: str) -> List[float]:
    """TODO: Call Bedrock Titan Embeddings v2 to get a vector for the text."""
    pass


def calculate_similarity(vec1: List[float], vec2: List[float]) -> float:
    """TODO: Calculate cosine similarity between two vectors."""
    # Hint: dot_product(a, b) / (norm(a) * norm(b))
    pass


def find_matches(query: str, catalog_items: List[Dict], catalog_vectors: List[List[float]], top_k: int = 3):
    """TODO: Find the top K semantic matches for a query."""
    pass


def main():
    # TODO: Implement semantic search pipeline
    # 1. Load catalog
    # 2. Generate embeddings for all catalog descriptions (cache these in a real app!)
    # 3. For each vague wish:
    #    a. Generate query embedding
    #    b. Find top matches
    #    c. Print/Store results
    pass


if __name__ == "__main__":
    main()
