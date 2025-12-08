# Day 8: Retrieval Augmented Christmas

## Story

The vector store hummed quietly in the corner of Santa's workshop, a crystalline structure of light and mathematics. It contained ten years of memories—every shared cookie, every pulled pigtail, every small act of kindness and mischief.

Santa stared at it with something like reverence. "It's beautiful. But it's just sitting there. A library with no librarian."

"Not for long," the Apprentice said, pulling up a new letter. "We have a test case. Timmy Anderson, age eight, from Whitehorse."

The letter was earnest, peppered with capital letters and exclamation points. Timmy wanted a Nintendo Switch. He claimed to be "super duper good." He'd mentioned helping his little sister with homework.

"He *sounds* like a nice kid," Santa said.

"He sounds like a nice kid," the Apprentice agreed. "But do we *know* he's a nice kid? Anyone can claim to be good."

Santa felt the weight of the question. In the old days, he would have simply *known*. But that magic was stretched thin now.

"We need to verify," Santa said slowly. "We need to check his history."

"Exactly." The Apprentice's fingers flew across the keyboard. "This is where RAG comes in. Retrieval Augmented Generation. We take Timmy's claims—'I share my stuff,' 'I helped my sister'—and use them as queries against the vector store."

"We're searching his past."

"We're *remembering* his past. We retrieve the relevant memories, inject them into the prompt, and suddenly the model has context."

The system took Timmy's claims and transformed them into semantic searches. Moments later, results surfaced like memories rising from deep water.

*March 15, 2024: Shared lunch with a friend who forgot theirs.*

*September 10, 2024: Helped little sister with homework. Spent 2 hours teaching basic math.*

Santa felt something warm bloom in his chest. "He wasn't lying."

They fed the retrieved memories into the model along with the original letter. The response felt almost like wisdom—noting Timmy's consistent pattern of generosity, his patience with his sister, his loyalty to friends.

"This is it," Santa said, his voice thick. "This is what we lost when the elves left. The ability to *know* these children."

"The technology doesn't replace the magic," the Apprentice said. "It just helps us remember."

Santa nodded, looking at Timmy's profile. A boy who shared his lunch. Who taught his sister math. Who believed in reindeer.

"Nintendo Switch," Santa said firmly. "He's earned it."

![Day 8: Retrieval Augmented Christmas](images/day08.png)

# Day 8: The RAG-Enhanced Profile

## Story

"Okay," Santa said, looking at the screen. "We have the vector store from Day 7. It knows who's been naughty and nice based on their behavior logs. But now we have a letter."

He held up a handwritten letter from **Tammy King**.

"Tammy says she's been 'super duper good' this year," Santa read. "She specifically mentions helping her little sister with homework and sharing her lunch. But... is she telling the truth?"

The Apprentice tapped the keyboard. "This is where Retrieval-Augmented Generation (RAG) comes in. We don't just ask the model 'Is Tammy good?' We take her claims from the letter, search our vector store for matching evidence, and *then* ask the model to verify it."

"So we're fact-checking children?" Santa raised an eyebrow.

"We're... verifying their self-assessments," the Apprentice corrected. "If Tammy says she helped her sister, and we find a log entry that says 'Helped little sister with homework,' then the model can confidently say: Verified."

"And if she says she cleaned her room, but the logs say she shoved everything under the bed?"

"Then the model will flag it as a discrepancy," the Apprentice grinned. "The Naughty-or-Nice list just got a lot more accurate."

![Day 8: The RAG-Enhanced Profile](images/day08.png)

> **Image Prompt Description**: A split-screen view of a high-tech "Truth-o-Meter." On one side, a handwritten letter from a child (Tammy) is being scanned. On the other side, a digital database scrolls through behavior logs. A central holographic brain (the LLM) is connecting a line between "I helped my sister" in the letter and a matching log entry, glowing green for "VERIFIED." Santa looks impressed.

---

## Learning Goal

Understand **Retrieval-Augmented Generation (RAG)** by combining unstructured user input (a letter) with structured retrieved data (behavior logs) to generate a fact-based response (a child profile).

## Participant Challenge

Write a script that:
1.  Reads **Tammy's letter** (`days/day08/input/letter_tammy.txt`).
2.  Extracts key claims (e.g., "I helped my sister").
3.  Simulates a vector search (using the `vector_store.json` from Day 7) to find relevant behavior logs.
4.  Uses an LLM (Bedrock) to generate a **Child Profile Summary** that confirms or denies the claims based on the evidence.

## Cost-Saving Tips

*   **Small Models for Extraction**: Use a cheaper model (like Claude 3 Haiku or Titan Text) for extracting claims from the letter.
*   **Local "Vector Search"**: Since our dataset is small, you don't need a real vector database yet. You can just load the JSON and do a simple keyword match or cosine similarity if you want to be fancy (but simple matching is fine for today).
*   **Prompt Caching**: If you were processing millions of letters, you'd cache the system prompt instructions.

## Tomorrow's Teaser

"Tammy is verified! But wait... we have a partial ID in this incident report, but the name is missing. Can we reconstruct the identity from scattered logs?"

---

## Technical Specifications

### Input Data
*   `days/day08/input/letter_tammy.txt`: A text file containing Tammy's letter to Santa.
*   `days/day07/output/vector_store.json`: The vector store created in Day 7 (or a mock version of it).

### Expected Output
*   `days/day08/output/tammy_profile_summary.txt`: A text file summarizing the child's profile.

#### Format
```markdown
# Child Profile: Tammy King

**Name:** Tammy King
**Age:** 11
**Location:** Cambridge Bay, Nunavut, Canada

## Wishlist
1. [Item 1]
2. [Item 2]
...

## Retrieved Behavior Records
- [Date] ([Category]): [Action]
...

## Assessment
[Model's analysis of whether the claims in the letter match the retrieved records.]

**Recommendation:** [Nice List / Naughty List / Needs Review]
```

### Implementation Steps
1.  **Load the Letter**: Read the text file.
2.  **Extract Claims**: Use an LLM or regex to find what the child claims they did.
3.  **Retrieve Evidence**: Search `vector_store.json` for matching `metadata['name']` and relevant `action` descriptions.
4.  **Generate Profile**: Construct a prompt that includes the letter content AND the retrieved logs, and ask the LLM to write the summary.

### Critical Concepts
*   **RAG (Retrieval-Augmented Generation)**: The pattern of retrieving external data to ground the LLM's response.
*   **Query Construction**: Converting "I helped my sister" into a search query.
*   **Context Injection**: Inserting the retrieved logs into the LLM's prompt context window.
*   **Evidence-Based Reasoning**: Asking the model to cite the specific logs that support its conclusion.
*   **Profile Synthesis**: Combining multiple data points into a coherent narrative.

### Prerequisites

*   Completion of Day 7 (Vector Store).
*   Access to Amazon Bedrock (Titan Embeddings + Claude).
*   Understanding of semantic search.

### Concepts Covered

* Retrieval-Augmented Generation (RAG)
* Query Construction
* Context Injection
* Evidence-Based Reasoning
* Profile Synthesis
