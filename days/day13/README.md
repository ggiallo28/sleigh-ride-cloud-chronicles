# Day 13: Enter Rudy (The Orchestrator)

## Story

The Priority Queue was a success, but Santa was still the bottleneck. He had to manually run the scripts, check the outputs, and make the final call.

"I need a manager," Santa said, rubbing his temples. "Someone who can take a high-level goal like 'Prepare for Christmas' and break it down into tasks. Someone who worries about the details so I don't have to."

"You need an Agent," the Apprentice said. "Not just a model that answers questions, but a system that pursues goals."

"Let's build one," Santa said. "Call him Rudy."

"Rudy?"

"Recursive Universal Distribution Yield. And give him a personality. I don't want a robot. I want a... Chief of Staff. Someone anxious enough to double-check everything, but brilliant enough to solve anything."

The Apprentice typed in the system prompt. *You are Rudy. You are anxious, hyper-organized, and slightly dramatic. Your goal is 100% efficiency. Failure is not an option.*

A text cursor blinked on the screen.

**Rudy**: "OH MY GARLAND! Do you have any idea what time it is? We are 4 milliseconds behind schedule! I need a status report on the plushies immediately, or we are all going to the coal mines!"

Santa grinned. "He's perfect."

![Day 13: Enter Rudy (The Orchestrator)](images/day13.png)

---

## Learning Goal

**Amazon Bedrock Agents and Persona Definition**

Today marks the beginning of **Phase 3: Agents**. An Agent is an LLM equipped with a persona, memory, and access to tools. The first step in building an agent is defining its **System Prompt** (or Persona). This instructions layer tells the model *who* it is, *how* it should behave, and *what* its boundaries are. A well-defined persona improves adherence to instructions and makes the user experience more engaging.

---

## Participant Challenge

Your challenge is to bring Rudy to life. You will take the persona definition (`rudy_persona.txt`) and configure a Bedrock Agent (or a simulated agent loop) that embodies this character. You must:
1.  Read the persona file.
2.  Construct a system prompt that enforces this personality.
3.  Interact with Rudy and get him to respond to a status check in character.

---

## Cost-Saving Tips

1.  **Prompt Efficiency**: You don't need pages of backstory. A few strong adjectives ("anxious," "dramatic") and a clear goal ("efficiency") are often enough for a powerful model to latch onto.

2.  **Session Reuse**: Just like in Day 10, keep the session alive. Don't re-initialize the agent for every message.

3.  **Model Choice**: For pure roleplay and orchestration, a model like Claude 3 Sonnet is excellent. Haiku is cheaper and faster but might be less "dramatic" unless prompted heavily.

4.  **Draft Mode**: When building Bedrock Agents in the AWS Console, use the "Test Alias" to iterate without publishing a new version every time.

---

## Tomorrow's Teaser

Rudy is great at worrying, but he can't actually *do* anything. He has no hands. He needs a partner who can reach into the database and move boxes.

---

## Technical Specifications

### Input Files

*   **rudy_persona.txt**: A text file defining Rudy's traits.

**Preview of rudy_persona.txt:**
```text
Name: Rudy
Role: Chief Orchestrator
Personality: Anxious, hyper-organized...
```

### Expected Output

*   **rudy_response.txt**: A transcript of Rudy's response to "How is the schedule looking?"

**Format Example:**
```text
User: How is the schedule looking?
Rudy: THE SCHEDULE?! *Hyperventilates* We are technically green, but the margin for error is microscopic! If one elf takes a bathroom break, we cascade into failure!
```

### Validation Criteria

*   The response reflects the "anxious/dramatic" personality.
*   The response acknowledges the role of "Orchestrator."
*   The system prompt clearly incorporates the input file content.

### Getting Started

1.  **Load Persona**: Read the text file.
2.  **Build Prompt**:
    ```text
    System: You are {name}. {personality}. {goal}.
    User: {input}
    ```
3.  **Invoke**: Send to the model.
4.  **Observe**: Tweak the prompt until he sounds sufficiently stressed out.

### Prerequisites

*   Completion of Phase 2 (RAG & Reasoning).
*   Understanding of System Prompts.

### Concepts Covered

*   Amazon Bedrock Agents
*   System Prompt Design
*   Persona Definition
*   Character-Based AI Interactions
*   Agent Architecture Fundamentals
