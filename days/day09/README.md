# Day 9: Complex Context Reconstruction

## Story

The "Nice List Vector Store" was working beautifully for simple queries. But then came the "Foam Incident."

It started with a frantic call from the Elf Safety Inspector. "We have a Code Red on the playground! Someone turned the snow into expanding foam!"

Santa pulled up the incident report. It was just a fragment—a corrupted text file recovered from a sticky server. "Subject ID 25 observed engaging in unauthorized alchemical experiments."

"Who is 25?" Santa asked.

The Apprentice checked the main database. "Corrupted. We lost the direct link between IDs and names in the crash."

"Great," Santa sighed. "So we have an ID but no name. Do we have any other logs?"

"I have a CSV file from the school registrar," the Apprentice said, "and a JSON log of library checkouts."

Santa looked at the three separate screens. "So, to find the culprit, we need to: 1. Read the incident report to get the ID. 2. Check the CSV to map the ID to a name. 3. Check the JSON log to see if that name has a history of... alchemy."

"It's a multi-hop query," the Apprentice nodded. "The answer isn't in any single document. It's in the *connection* between them. We need to teach the model to be a detective."

Santa cracked his knuckles. "Let's connect the dots."

![Day 9: Complex Context Reconstruction](images/day09.png)



---

## Learning Goal

**Advanced RAG and Query Decomposition**

Real-world data is rarely in one clean place. It's scattered across databases, logs, and documents. Today you'll learn **Multi-Hop Reasoning** (or "Complex Query Decomposition"). This is an advanced RAG pattern where the answer requires retrieving information from Source A, using that to query Source B, and finally synthesizing the result. You'll move beyond simple "search and summarize" to building a system that can follow a trail of evidence.

---

## Participant Challenge

Your challenge is to solve the "Foam Incident" mystery. You have three disparate data sources:
1.  `incident_fragment.txt` (Contains the suspect's ID).
2.  `id_mapping.csv` (Maps IDs to Names).
3.  `activity_log.json` (Shows recent activities for various children).

You must write a script that:
1.  Extracts the ID from the incident report.
2.  Looks up the name associated with that ID.
3.  Retrieves the recent activity for that name.
4.  Synthesizes a final report explaining *who* did it and *what* they were doing beforehand that might have led to the incident.

---

## Cost-Saving Tips

1.  **Decompose before you search**: Don't just throw all three files into the context window (that's expensive and noisy). Use a small prompt to extract the ID first ("What is the Subject ID in this text?"). Then use that ID for a precise lookup.

2.  **Structured Data Lookup**: For the CSV and JSON, you don't necessarily need an LLM. You can use Python (pandas/json) to do the exact lookup. Use the LLM only for the unstructured parts (reading the report, synthesizing the final narrative). This is a "Tool Use" or "Agentic" pattern.

3.  **Chain of Thought**: Ask the model to "think step-by-step." This often improves accuracy on multi-step reasoning tasks without requiring a larger, more expensive model.

4.  **Keep intermediate outputs small**: You only need to pass the *result* of step 1 to step 2, not the whole conversation history.

---

## Tomorrow's Teaser

We've mastered the past (logs) and the present (letters). But what about the future? Santa needs to predict toy trends before they happen to optimize the workshop's supply chain.

---

## Technical Specifications

### Input Files

*   **incident_fragment.txt**: Text file with the incident details and Subject ID.
*   **id_mapping.csv**: CSV file mapping IDs to Names.
*   **activity_log.json**: JSON file with timestamped activities.

### Expected Output

*   **investigation_report.json**: A JSON file with the findings.

**Format Example:**
```json
{
  "suspect_id": "9482",
  "suspect_name": "Calvin",
  "corroborating_evidence": "Borrowed 'Chemistry for Beginners' from library",
  "conclusion": "Calvin (ID 9482) is the likely culprit, as he was identified in the report and had recently acquired chemistry materials."
}
```

### Validation Criteria

*   The script correctly identifies "9482" as the ID.
*   The script correctly maps "9482" to "Calvin".
*   The script correctly links Calvin to the "Chemistry for Beginners" activity.
*   The final report synthesizes these three facts into a coherent conclusion.

### Getting Started

1.  **Step 1 (Extraction)**: Read `incident_fragment.txt`. Use regex or a simple LLM prompt to extract the ID.
2.  **Step 2 (Lookup)**: Load `id_mapping.csv` into a pandas DataFrame or dictionary. Find the name for the extracted ID.
3.  **Step 3 (Correlation)**: Load `activity_log.json`. Filter for entries matching the name found in Step 2.
4.  **Step 4 (Synthesis)**: Feed the findings to the LLM: "Subject ID {id} (Name: {name}) was involved in an incident. Their recent activity was {activity}. Write a brief conclusion."

### Prerequisites

*   Completion of Days 1-8.
*   Basic data manipulation (CSV/JSON in Python).
*   Understanding of modular code structure.

### Concepts Covered

*   Multi-Hop Reasoning
*   Complex Query Decomposition
*   Tool Use / Agentic Patterns
*   Structured Data Lookup
*   Chain of Thought

