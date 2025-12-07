# Day 7: The Nice List Vector Store

## Story

The semantic search engine was a hit. Santa could now find "something red that goes fast" in milliseconds. But as he looked at the dashboard, a deeper problem emerged.

"We can find toys," Santa said, leaning back in his chair. "But can we find *truth*?"

The Apprentice paused. "That's deep, Santa."

"I mean context," Santa clarified. "I have a letter here from Timmy. He says he's been 'very good.' But my memory isn't what it used to be. I have ten years of behavior logs stored in the archives—millions of incidents. 'Shared a cookie,' 'Pulled a pigtail,' 'Helped grandma.' It's all there, but it's just... text. Unstructured, messy text."

"You want to search it?"

"I want to *know* it," Santa said. "When Timmy asks for a console, I don't just want to know if we have consoles. I want to know if Timmy *deserves* a console. I need to pull up every relevant thing he's done—not just by keyword, but by meaning. If he says he's 'helpful,' I want to find instances of helpfulness, even if the log says 'assisted' or 'volunteered.'"

The Apprentice nodded slowly. "You need a Knowledge Base. A Vector Store. We take all those behavior logs, turn them into embeddings—just like the toys—and store them in a way that lets us retrieve the most relevant memories instantly."

Santa looked at the massive pile of digital logs. "So we're building an external brain?"

"Exactly. The Nice List isn't just a list anymore. It's a database of semantic memories."

---

## Learning Goal

**Knowledge Bases and Vector Indexing**

Today you will build the foundation for a **RAG (Retrieval Augmented Generation)** system. You've learned about embeddings (Day 6); now you'll learn how to store and index them efficiently. A **Vector Store** (or Vector Database) allows you to save generated embeddings along with their metadata so they can be searched later. This is the "Long-Term Memory" of an AI application. Instead of feeding all data to the model every time (which is expensive and limited by context windows), you index it once and retrieve only what you need.

---

## Participant Challenge

Your challenge is to build the "Nice List Vector Store." You will take a dataset of behavior logs (`behavior_logs.json`), generate embeddings for each record, and save them into a local vector index. While production systems use databases like Pinecone or Milvus, for this challenge you will build a simple local index (using a JSON file or a library like FAISS/ChromaDB if you prefer) to understand the mechanics.

---

## Cost-Saving Tips

1.  **Index once, query many**: Generating embeddings is the expensive part. Do it once and save the result. Never re-embed your static dataset for every query.

2.  **Batch your embeddings**: Send behavior logs to the embedding model in batches (e.g., 10-20 at a time) to reduce network overhead and potentially optimize throughput.

3.  **Store metadata separately**: You don't need to embed the *entire* JSON object. Embed the `action` and `details` text, but keep the `date` and `category` as metadata. This keeps the vector cleaner and saves tokens.

4.  **Use a local vector store**: For development and small datasets, use a local library (like FAISS, Chroma, or even a simple numpy array) instead of spinning up a managed cloud vector database instance, which often has hourly costs.

---

## Tomorrow's Teaser

The memory bank is built. Now, a letter arrives from a boy named Timmy who claims to be an angel. It's time to put the system to the test and see if the AI can catch a liar.

---

## Technical Specifications

### Input Files

*   **behavior_logs.json**: A JSON file containing historical behavior records for various children.

**Preview of behavior_logs.json:**
```json
[
  {
    "id": "101",
    "name": "Timmy",
    "action": "Shared lunch with a friend...",
    "category": "Nice"
  },
  ...
]
```

### Expected Output

*   **vector_store.json** (or a directory of index files): A file containing the vectors and associated metadata for the behavior logs.

**Format Example (for simple JSON store):**
```json
[
  {
    "id": "101",
    "embedding": [0.12, -0.05, ...],
    "metadata": { "name": "Timmy", "action": "..." }
  },
  ...
]
```

### Validation Criteria

*   The script reads the `behavior_logs.json` file.
*   Embeddings are generated for the `action` + `details` fields using Amazon Titan Embeddings.
*   The output file contains vectors for all input records.
*   The vectors are of the correct dimension (e.g., 1536 for Titan).

### Getting Started

1.  **Load the data**: Read the JSON file.
2.  **Prepare the text**: For each record, create a text string to embed (e.g., `f"{record['action']} {record['details']}"`).
3.  **Generate embeddings**: Use Bedrock to get the vector for each string.
4.  **Structure the index**: Create a list of objects where each object has the original ID, the metadata, and the vector.
5.  **Save to disk**: Write this list to a file. This is your "database."

### Prerequisites

*   Completion of Day 6 (Embeddings).
*   Understanding of JSON.
*   Access to Amazon Titan Embeddings.
