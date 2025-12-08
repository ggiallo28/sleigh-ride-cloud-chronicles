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

---

## Learning Goal

**Basic RAG (Retrieval-Augmented Generation)**

Today you'll connect a foundation model to external knowledge using RAG. Language models have limited context windows and no memory of your specific data. By *retrieving* relevant information from a vector store and *augmenting* the prompt with that context, you give the model access to knowledge it wouldn't otherwise have. The workflow: (1) receive a query, (2) search the vector store for relevant records, (3) inject those records into the prompt, (4) generate an informed response. In Project Sleigh-Ride, RAG lets Santa verify children's claims against historical behavior records.

---

## Participant Challenge

Your challenge is to implement basic RAG. You'll take a letter from a child who claims to have been good, extract the key behavioral claims, query the vector store from Day 7 to retrieve relevant historical records, and use a foundation model to synthesize a comprehensive profile combining the letter with retrieved behavior data. The goal is to demonstrate that augmenting context with retrieved memories enables informed judgments.

---

## Cost-Saving Tips

1.  **Retrieve selectively**: Don't dump your entire vector store into the prompt. Retrieve only the top 3-5 most relevant records to reduce token costs.

2.  **Cache retrieval results**: If multiple queries relate to the same child, cache their behavior records rather than re-querying.

---

## Tomorrow's Teaser

Timmy's profile is complete, but Santa realizes the information is scattered—letters, behavior logs, address histories. Tomorrow, he learns to weave multiple data sources into a single tapestry of truth.

---

## Technical Specifications

### Input Files

*   **letter_timmy.txt**: A letter from Timmy Anderson claiming to have been good.
*   **vector_store.json** (from Day 7): The vector index containing behavior log embeddings.

**Preview of letter_timmy.txt:**
```
--- START LETTER ---
From: Timmy Anderson
Address: 42 Snowflake Lane, Whitehorse, Yukon, Y1A 3T7, Canada
Date: 2024-12-08

Dear Santa,

Hi! It's me, Timmy! I'm 8 years old...
I've been REALLY good this year, Santa. Like, super duper good. 
I always share my stuff and I help people all the time...
--- END LETTER ---
```

### Expected Output

*   **timmy_profile_summary.txt**: A comprehensive profile combining letter content with retrieved behavior records.

**Format Example:**
```markdown
# Child Profile: Timmy Anderson

**Name:** Timmy Anderson  
**Age:** 8  
**Location:** Whitehorse, Yukon, Canada

## Wishlist
1. Nintendo Switch
2. Mario Kart game
3. Lego sets (space themed)

## Retrieved Behavior Records
- March 15, 2024 (Nice): Shared lunch with a friend
- September 10, 2024 (Nice): Helped sister with homework

## Assessment
Claims verified against historical records.
**Recommendation:** Nice List
```

### Validation Criteria

*   The script loads the letter and vector store from Day 7.
*   Behavioral claims are extracted from the letter.
*   Relevant records are retrieved using semantic search.
*   The output combines letter content with retrieved evidence.
*   A final recommendation is provided.

### Getting Started

1.  **Load the letter**: Read the letter file.
2.  **Load vector store**: Load the index from Day 7.
3.  **Extract claims**: Identify behavioral claims from the letter.
4.  **Retrieve records**: Query the vector store for each claim.
5.  **Build RAG prompt**: Combine letter + retrieved records.
6.  **Generate profile**: Call the LLM with augmented context.
7.  **Save output**: Write the profile to file.

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
