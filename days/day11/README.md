# Day 11: The Moral Compass

## Story

The "Naughty or Nice" algorithm was running smoothly until it hit Case #402.

**Subject**: Jenny.
**Action**: Painted the family cat blue.
**Algorithm Verdict**: NAUGHTY (Property Damage + Animal Harassment).

Santa stared at the screen. "She painted the cat?"

"Bright blue," the Apprentice confirmed. "With non-toxic, washable finger paint."

"Why?"

"According to the interview, she thought the cat looked sad. She wanted to make him 'happy like the sky'."

Santa sat back. "So, the action was destructive, but the intention was pure compassion. The algorithm only sees the 'what'. It misses the 'why'."

"It's a binary classifier," the Apprentice shrugged. "It doesn't do nuance."

"Christmas is nothing *but* nuance!" Santa exclaimed. "If we punish a child for trying to be kind, we're the ones being naughty. We need a system that can think through the situation. One that weighs the intent against the outcome."

"Chain of Thought," the Apprentice said. "We don't just ask for a verdict. We ask the model to 'think step-by-step'. First, analyze the action. Second, analyze the intent. Third, consider the consequences. *Then* give a verdict."

Santa nodded. "Teach it to think like a parent, not a judge."

![Day 11: The Moral Compass](images/day11.png)

---

## Learning Goal

**Chain-of-Thought (CoT) Prompting**

Foundation models are powerful, but they can jump to conclusions if asked to answer complex questions immediately. **Chain-of-Thought** is a prompt engineering technique where you instruct the model to "think step-by-step" or break down its reasoning before providing a final answer. This significantly improves performance on tasks requiring logic, math, or ethical reasoning, as it allows the model to generate its own intermediate context.

---

## Participant Challenge

Your challenge is to build the "Moral Compass." You will process a list of ambiguous scenarios (`ambiguous_scenarios.json`) where the line between Naughty and Nice is blurry. You must write a script that uses Chain-of-Thought prompting to:
1.  Analyze the **Action** (what happened).
2.  Analyze the **Intent** (why it happened).
3.  Evaluate the **Outcome** (harm done vs. good intended).
4.  Provide a nuanced verdict ("Nice", "Naughty", or "Complex/Forgiven") with a clear explanation.

---

## Cost-Saving Tips

1.  **Zero-Shot CoT**: You don't always need to provide examples. Simply appending "Let's think step by step" to your prompt is often enough to trigger reasoning chains in capable models (like Claude 3 Sonnet).

2.  **Stop Sequences**: If you only want the reasoning and the verdict, you can tell the model to stop generating after it outputs the JSON verdict, preventing it from rambling on.

3.  **Use lighter models for simple logic**: While deep ethical reasoning might need a big model, many "common sense" checks can be done by smaller models (like Haiku) if the prompt is structured well with clear steps.

4.  **Structured Output**: Ask the model to output the reasoning steps in specific JSON fields (e.g., `{"step_1_analysis": "...", "step_2_intent": "..."}`). This makes the "thought process" parsable and usable in your application.

---

## Tomorrow's Teaser

Reasoning is great, but it's slow. Santa needs to make decisions for millions of children in real-time. We need to scale up our processing power without melting the servers.

---

## Technical Specifications

### Input Files

*   **ambiguous_scenarios.json**: A list of scenarios with action and context.

**Preview of ambiguous_scenarios.json:**
```json
[
  {
    "child_name": "Jenny",
    "action": "Painted the family cat blue.",
    "context": "She thought the cat looked sad..."
  },
  ...
]
```

### Expected Output

*   **moral_verdicts.json**: A JSON file containing the reasoning and final decision for each case.

**Format Example:**
```json
[
  {
    "child_name": "Jenny",
    "reasoning": "1. Action: Painting a cat is generally bad... 2. Intent: She wanted to cheer it up... 3. Outcome: Paint was washable...",
    "verdict": "NICE (with a warning)"
  },
  ...
]
```

### Validation Criteria

*   The script processes all scenarios in the input file.
*   The output demonstrates "step-by-step" reasoning (not just a one-word answer).
*   The verdict for Jenny (Blue Cat) acknowledges the good intent (not just "Naughty").
*   The verdict for Billy (Stolen Bread) acknowledges the compassion for the dog.

### Getting Started

1.  **Load the data**: Read the JSON file.
2.  **Design the Prompt**:
    ```text
    Scenario: {action}
    Context: {context}
    
    Task: Evaluate if this behavior is Naughty or Nice.
    Instructions:
    1. Analyze the action's severity.
    2. Analyze the child's intent.
    3. Weigh the harm against the good.
    4. Provide a final verdict.
    
    Output format: JSON with fields 'reasoning' and 'verdict'.
    ```
3.  **Loop and Invoke**: Send each scenario to the model.
4.  **Save Results**: Collect the responses and save to `moral_verdicts.json`.

### Prerequisites

*   Completion of Days 1-10.
*   Understanding of Prompt Engineering (Zero-Shot vs Few-Shot).

### Concepts Covered

*   Chain-of-Thought (CoT) Prompting
*   Zero-Shot vs Few-Shot Reasoning
*   Structured Output Parsing
*   Ethical Reasoning with LLMs
*   Multi-Step Analysis Prompts
