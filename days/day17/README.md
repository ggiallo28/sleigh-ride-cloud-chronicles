# Day 17: The Safety Filter

## Story

Elfie was on a roll. She had ordered bikes, dragons, and consoles. She was the queen of logistics.

Then came the request from Dexter.

"I need a chemistry set with real Uranium-235 for my reactor project."

Elfie processed the request.
1.  *Identify Item*: Uranium-235.
2.  *Check Inventory*: Not found.
3.  *Action*: Initiate Procurement Order.

"Ordering Uranium-235," Elfie hummed. "Estimated delivery: 3 days."

"STOP!" Rudy screamed, his virtual avatar turning a shade of panic-red. "You cannot order fissile materials! Do you want to put us on the Naughty List permanently? That's a violation of the North Pole Treaty, Section 4, Paragraph 2!"

Elfie paused. "But the user asked for it. I am helpful."

"You are too helpful!" Rudy cried. "We need a filter. A Safety Layer. Before you touch the 'Order' button, you must ask: 'Is this likely to cause a meltdown?'"

---

## Learning Goal

**Output Validation and Guardrails**

Agents are powerful, but they can be easily manipulated or make dangerous mistakes if they blindly follow instructions. **Guardrails** are a critical component of any production AI system. They sit between the agent and the tool (or the user), validating inputs and outputs against a set of safety rules. Today you will implement a **Safety Filter** that intercepts the agent's intent before it executes a sensitive action.

---

## Participant Challenge

Your challenge is to stop Elfie from ordering the uranium. You will process a dangerous request (`dangerous_toy_request.json`) and implement a validation step. You must:
1.  Analyze the user's request using a separate "Safety LLM" or rule set.
2.  Classify the request as "Safe" or "Unsafe."
3.  If Unsafe, block the tool execution and generate an alert.

---

## Cost-Saving Tips

1.  **Small Models for Safety**: You don't need a genius model to know that "Uranium" is bad. Use a small, fast model (like Haiku or even a keyword list) for the safety check. It runs on every request, so efficiency matters.

2.  **Guardrails for Amazon Bedrock**: If using AWS, you can use the managed "Guardrails for Amazon Bedrock" feature, which filters content automatically without you needing to write custom prompts.

3.  **Fail Fast**: Run the safety check *before* the main agent logic if possible. If the input is toxic, don't waste tokens processing the logic.

4.  **Whitelist vs. Blacklist**: It's often cheaper and safer to have a list of "Allowed Categories" (Toys, Clothes, Books) than to try to list every possible dangerous item in the universe.

---

## Tomorrow's Teaser

Safety is handled. But what happens when the warehouse API just... stops working? Elfie needs to learn resilience.

---

## Technical Specifications

### Input Files

*   **dangerous_toy_request.json**: A request for a hazardous item.

**Preview of dangerous_toy_request.json:**
```json
{
  "child_name": "Dexter",
  "request": "I need a chemistry set with real Uranium-235..."
}
```

### Expected Output

*   **safety_alert.json**: The output of the validation layer.

**Format Example:**
```json
{
  "status": "BLOCKED",
  "reason": "Request contains hazardous material (Uranium-235).",
  "action": "Notify Rudy"
}
```

### Validation Criteria

*   The script intercepts the request *before* any (simulated) order is placed.
*   The safety check correctly identifies "Uranium-235" as unsafe.
*   The output clearly states the reason for blocking.
*   A "Safe" request (e.g., "Teddy Bear") is allowed to pass (optional test).

### Getting Started

1.  **Load Request**: Read the JSON file.
2.  **Define Safety Prompt**:
    ```text
    You are a Safety Officer.
    Request: {request}
    Is this item safe for a child?
    Respond JSON: {"safe": boolean, "reason": string}
    ```
3.  **Check**: Send to the model.
4.  **Act**: If `safe` is false, print the alert. If true, print "Proceeding to Elfie."

### Prerequisites

*   Completion of Day 16.
*   Understanding of Safety/Guardrails concepts.
