# Day 12: The Priority Queue

## Story

The countdown clock on the wall ticked louder. T-minus 12 days.

The "Nice List Vector Store" was indexed. The "Moral Compass" was calibrating. But the sheer volume of incoming requests was overwhelming the manufacturing floor.

"We have 50,000 requests pending," the Apprentice reported, voice tight. "And the fabrication machines can only handle 40,000 before the deadline."

Santa looked at the queue. It was a flat list, sorted by timestamp. "So, the kid who asked for a replacement video game controller five minutes ago is ahead of the child in the hospital who asked for a teddy bear yesterday?"

"Technically, yes. First in, first out."

"That's not how compassion works," Santa said, standing up. "We need Triage. We need to prioritize. A cold puppy needs a blanket *now*. A broken toy can wait."

"But how do we quantify 'need'?" the Apprentice asked. "Is a bike more important than a video game? Is a hug more important than a bike?"

"We ask the model to feel," Santa said. "We give it a rubric. Urgency. Emotional Impact. Necessity. And we ask it to rank them. We're not just building a queue anymore. We're building a Priority Queue based on the Spirit of Christmas."

![Day 12: The Priority Queue](images/day12.png)

---

## Learning Goal

**Qualitative Reasoning and Ranking**

LLMs excel at **Qualitative Reasoning**—evaluating subjective criteria that are hard to capture with traditional code. In this challenge, you will use the model to assign a numerical "Priority Score" to text requests based on nuanced factors like urgency, emotional weight, and need. This pattern is widely used in customer support triage, content moderation, and lead scoring.

---

## Participant Challenge

Your challenge is to build the "Triage System." You will process a batch of gift requests (`gift_requests.json`) that vary from trivial to critical. You must write a script that:
1.  Analyzes each request against a set of priority criteria.
2.  Assigns a **Priority Score** (1-5, where 5 is Critical).
3.  Provides a brief justification for the score.
4.  Sorts the final list so the most urgent cases are at the top.

---

## Cost-Saving Tips

1.  **Single-Token Scoring**: You can ask the model to output *just* the number (e.g., "5") to save tokens, then parse it. However, asking for a short reason ("5 - Medical urgency") usually improves the accuracy of the score itself (Chain of Thought).

2.  **Batch Ranking**: Instead of scoring one by one, send a batch of 5-10 requests to the model and ask it to "Rank these from highest to lowest priority." This is often more efficient and allows the model to compare items relative to each other.

3.  **Use a Rubric**: Include a clear rubric in your prompt (e.g., "5 = Health/Safety, 4 = Emotional Well-being, 1 = Luxury/Greed"). This reduces hallucination and keeps the scoring consistent without needing a massive model.

4.  **Hybrid Sort**: Use the LLM for the coarse score (1-5), then use traditional code (like timestamp) to sort within those buckets. Don't make the LLM do the final sorting of the whole list.

---

## Tomorrow's Teaser

The queue is sorted, but the workload is still too high for one person (or one script). Santa realizes he needs a team of specialized helpers who can work autonomously.

---

## Technical Specifications

### Input Files

*   **gift_requests.json**: A list of requests with context.

**Preview of gift_requests.json:**
```json
[
  {
    "child_name": "Sarah",
    "request": "My puppy is shivering...",
    "context": "Urgent need for a pet."
  },
  ...
]
```

### Expected Output

*   **prioritized_list.json**: The same list, but sorted by priority (descending) and including the score/reasoning.

**Format Example:**
```json
[
  {
    "child_name": "Emily",
    "request": "I'm in the hospital...",
    "priority_score": 5,
    "reasoning": "Medical context and high emotional need."
  },
  {
    "child_name": "Sarah",
    "request": "My puppy is shivering...",
    "priority_score": 4,
    "reasoning": "Animal welfare concern."
  },
  ...
]
```

### Validation Criteria

*   The output list is sorted by `priority_score` in descending order.
*   Emily (Hospital) is ranked higher than Tommy (Bike).
*   Sarah (Puppy) is ranked higher than Billy (Controller).
*   Jack (Greedy request) is ranked lowest.
*   Each entry has a valid reasoning string.

### Getting Started

1.  **Load the data**: Read `gift_requests.json`.
2.  **Define the Rubric**:
    *   5: Critical (Health, Safety, Crisis)
    *   4: High (Emotional Distress, Basic Needs)
    *   3: Standard (Normal Wishes)
    *   2: Low (Minor wants, replacements)
    *   1: Trivial (Greed, impossible items)
3.  **Prompt**: "Evaluate this request based on the rubric. Return JSON with 'score' and 'reason'."
4.  **Score**: Loop through the list and apply the prompt.
5.  **Sort**: Use Python's `sort` or `sorted` function with a key (e.g., `key=lambda x: x['priority_score'], reverse=True`).
6.  **Save**: Write the result to `prioritized_list.json`.

### Prerequisites

*   Completion of Days 1-11.
*   Basic Python sorting.
*   Prompt Engineering for classification.

### Concepts Covered

*   Qualitative Reasoning with LLMs
*   Priority Scoring and Ranking
*   Rubric-Based Classification
*   JSON Output Parsing
*   List Sorting in Python
