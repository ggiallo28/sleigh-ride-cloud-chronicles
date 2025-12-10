# Day 10: Rudy's Memory (Short Term)

## Story

The "Santa Chatbot" was technically working. It could answer questions. It could look up toys. It could even check the Naughty List.

But it had the attention span of a goldfish.

Santa watched the beta test logs scroll by.

**User**: "Hi, I'm Sally."
**Bot**: "Ho ho ho! Hello, Sally!"
**User**: "I want a pony."
**Bot**: "A pony is a wonderful wish!"
**User**: "What's my name?"
**Bot**: "I'm sorry, I don't know your name. Who are you?"

Santa facepalmed. "It forgot her name in two seconds. How can we build a relationship if we don't remember anything?"

"It's stateless," the Apprentice explained. "Every time Sally sends a message, the model treats it as a brand new conversation. It doesn't know that 'I want a pony' came from the same person who said 'I'm Sally'."

"We need to give it a memory," Santa said. "Short-term memory. Just enough to hold a conversation."

"We can append the chat history to the prompt," the Apprentice suggested. "We send the previous messages back to the model with every new question. That way, it sees the whole context."

"Like carrying a notebook?"

"Exactly. But the notebook has a limit. We can't carry it forever."

"Let's worry about forever later," Santa said. "Right now, I just want it to remember Sally."

![Day 10: Rudy's Memory (Short Term)](images/day10.png)
---

## Learning Goal

**Session State Management**

Foundation models are **stateless**. They do not remember previous interactions. To build a chatbot, you must manage the **Session State** yourself. This involves storing the conversation history (User: "Hi", Assistant: "Hello") and sending relevant parts of it back to the model with each new prompt. This allows the model to reference past information ("My name is Sally") to answer current questions ("What is my name?").

---

## Participant Challenge

Your challenge is to fix the amnesiac chatbot. You will process a simulated conversation (`chat_history.json`) where a user introduces themselves and then asks questions relying on that context. You must write a script that:
1.  Maintains a `history` list.
2.  Iterates through the user messages.
3.  For each message, constructs a prompt that includes the *entire* conversation history so far.
4.  Generates a response that proves the model "remembers" the details.

---

## Cost-Saving Tips

1.  **Limit the history**: You don't need to send the *entire* conversation since the beginning of time. Sending the last 5-10 turns is usually enough for immediate context. This is called a "sliding window."

2.  **Summarize older context**: Instead of dropping old messages, ask the model to summarize them into a single "Context" paragraph and keep that at the top of the prompt. This saves tokens while preserving key facts.

3.  **Use the `Converse` API**: If using Amazon Bedrock, the `Converse` API handles some of the message formatting for you, making it easier to structure the turn-by-turn history.

4.  **Client-side state**: Store the history in your application (or a lightweight database like Redis), not in the model itself (which isn't possible).

---

## Tomorrow's Teaser

Short-term memory is great, but what if we need to remember something Sally said *last year*? Or what if the conversation gets so long it crashes the system? We need a more permanent solution.

---

## Technical Specifications

### Input Files

*   **chat_history.json**: A list of user messages in chronological order.

**Preview of chat_history.json:**
```json
[
  { "role": "user", "content": "Hi, I'm Sally from Chicago." },
  { "role": "user", "content": "I want a pony." },
  { "role": "user", "content": "What was my name again?" }
]
```

### Expected Output

*   **chat_session.log**: A text file showing the full conversation transcript (User and Bot).

**Format Example:**
```text
User: Hi, I'm Sally from Chicago.
Bot: Ho ho ho! Hello, Sally from Chicago!

User: I want a pony.
Bot: A pony is a big wish! I'll see what I can do.

User: What was my name again?
Bot: Your name is Sally.
```

### Validation Criteria

*   The bot correctly identifies the user's name ("Sally") in the final response.
*   The bot correctly identifies the user's location ("Chicago") if asked.
*   The script demonstrates that the history is being passed to the model (the responses depend on previous inputs).

### Getting Started

1.  **Initialize**: Create an empty list `messages = []`.
2.  **Loop**: Iterate through the input JSON.
3.  **Update**: Append the new user message to `messages`.
4.  **Prompt**: Pass the `messages` list to the Bedrock `Converse` API (or format it as a string block).
5.  **Response**: Get the model's response, print it, and append it to `messages` (so the model remembers its own answers too!).

### Prerequisites

*   Completion of Days 1-9.
*   Understanding of lists/arrays.
*   Familiarity with the Bedrock `Converse` API (recommended) or prompt formatting.

### Concepts Covered

*   Session State Management
*   Stateless vs. Stateful Systems
*   Context Window Management (Sliding Window)
*   Conversation History Formatting
*   Chatbot Interaction Loops

