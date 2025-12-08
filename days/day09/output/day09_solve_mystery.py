# /// script
# dependencies = [
#   "boto3",
#   "pandas",
# ]
# ///

import boto3
import json
import pandas as pd
import re

# ------------------------------
# Day 9 – Complex Context Reconstruction
# Starter Script
# ------------------------------

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

INCIDENT_FILE = "input/incident_fragment.txt"
ID_MAPPING_FILE = "input/id_mapping.csv"
ACTIVITY_LOG_FILE = "input/activity_log.json"
OUTPUT_FILE = "output/investigation_report.json"

# TODO: Create Bedrock client
bedrock = None

def extract_id_from_text(text):
    """TODO: Extract the Subject ID (4 digits) from the text."""
    # Hint: Use regex or a simple LLM prompt
    pass

def get_name_for_id(subject_id):
    """TODO: Look up the name in the CSV file."""
    pass

def get_activity_for_name(name):
    """TODO: Filter the JSON log for this name."""
    pass

def synthesize_report(subject_id, name, activity):
    """TODO: Use Bedrock to write the final investigation report."""
    pass

def main():
    print("🕵️‍♂️ Starting Investigation...")
    
    # 1. Read the incident report
    with open(INCIDENT_FILE, 'r') as f:
        incident_text = f.read()
    
    # 2. Extract ID
    subject_id = extract_id_from_text(incident_text)
    print(f"🔍 Extracted Subject ID: {subject_id}")
    
    if not subject_id:
        print("❌ Failed to extract ID.")
        return

    # 3. Lookup Name
    name = get_name_for_id(subject_id)
    print(f"👤 Identified Suspect: {name}")

    # 4. Find Activity
    activity = get_activity_for_name(name)
    print(f"📅 Recent Activity: {activity}")

    # 5. Synthesize Report
    report = synthesize_report(subject_id, name, activity)
    
    # 6. Save Output
    if report:
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"✅ Investigation Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
