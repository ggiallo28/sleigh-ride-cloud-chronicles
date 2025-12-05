# Day 6: The Vague Wish

## Story

The validation gate was working perfectly. The chunking system was humming along, digesting ten-page essays into concise summaries. For the first time in weeks, the North Pole workshop felt like it was under control.

Santa sat back in his chair, sipping cocoa, feeling almost relaxed. "We might actually pull this off," he said.

"Don't jinx it," the Apprentice warned, though they were smiling too.

Then a new notification pinged on the main screen. A single letter. Short. Simple.

*Dear Santa,*
*I want something red that goes fast.*
*Love, Leo (age 5)*

Santa stared at it. "Something red that goes fast."

"Well," the Apprentice said, "that's... specific."

"Is it?" Santa asked. "Is it a fire truck? A race car? A red sled? A superhero cape? A rocket?" He sighed. "In the old days, I'd just *know*. I'd look at the child's history, their other toys, the feeling in the letter. But the model? The model just sees words."

"If we search our inventory for 'something red that goes fast'," the Apprentice said, typing a query, "we get..."

The screen flashed: **NO EXACT MATCH FOUND.**

"Of course," the Apprentice sighed. "Because no product is named 'something red that goes fast'. We have 'Turbo Racer 3000' and 'Red Fire Engine' and 'Supersonic Sled'. But the keywords don't match."

"So we're stuck," Santa said. "Unless we can teach the machine to understand what the words *mean*, not just what they *are*."

The Apprentice's eyes lit up. "Embeddings."

"Bless you," Santa said.

"No, it's a technology! Embeddings turn text into numbers. Vectors. They map meaning in a multi-dimensional space. 'King' is close to 'Queen'. 'Red' and 'Fast' would be close to 'Race Car' and 'Fire Truck'."

Santa leaned forward. "So we don't need exact keywords? We can search by... concept?"

"Exactly. We turn Leo's wish into a vector. We turn every toy in our catalog into a vector. Then we just find the toys that are mathematically closest to the wish."

They set to work. The Apprentice explained how to generate embeddings for the entire toy catalog—turning descriptions of dolls, trucks, and games into long strings of numbers. Then they took Leo's vague wish—"something red that goes fast"—and converted it too.

When they ran the comparison, the system didn't return an error. It returned a list.

1. **Turbo Fire Truck** (Score: 0.89) - "A bright red fire engine with working sirens and high-speed wheels."
2. **Lightning Racer** (Score: 0.87) - "Red sports car, built for speed."
3. **Rocket Sled** (Score: 0.82) - "Aerodynamic red sled for fast downhill racing."

Santa looked at the list, then at Leo's profile. "He lives in a city. No hills for sleds. He loves helping people. It's the fire truck."

He selected the item. The system logged the match.

"It felt like magic," Santa said softly. "It understood what he meant, not just what he said."

"That's the power of semantic search," the Apprentice said. "It bridges the gap between human intent and database records."

Santa smiled, watching the queue of vague wishes—"something cuddly," "a game for my family," "cool space stuff"—suddenly finding their perfect matches. "It's not just search," he said. "It's understanding."

---

![Day 6: The Vague Wish](images/day06.png)

---

## Learning Goal

**Embeddings and Semantic Search**

Today you'll learn how to bridge the gap between human language and structured data using *embeddings*. Traditional search relies on keyword matching (finding "car" in "race car"), which fails when users use vague or conceptual language ("something fast"). Embeddings convert text into numerical vectors where similar concepts are mathematically close together. By calculating the *cosine similarity* between a user's query vector and your product vectors, you can perform *semantic search*—finding items that match the *meaning* of the request, even if they don't share a single keyword. In Project Sleigh-Ride, this allows Santa to interpret vague wishes like "something cool for drawing" and match them to "Deluxe Art Set" with high accuracy.

---

## Participant Challenge

Participants will practice today's capability using the materials provided for this day. You will build a semantic search system that matches vague children's wishes to specific products in the toy catalog. You'll generate embeddings for the catalog items and the incoming queries, then use cosine similarity to find the best matches. The goal is to demonstrate that you can retrieve relevant results based on *intent* rather than just keywords, solving the "vocabulary mismatch" problem that plagues traditional search systems.

---

## Cost-Saving Tips

1. **Cache your embeddings**: Generating embeddings costs money. Never re-generate embeddings for static data (like your product catalog). Generate them once, save them (in a vector store or simple JSON/CSV), and reuse them.

2. **Use smaller embedding models**: For simple semantic matching, you don't always need the largest, most expensive embedding model. Titan Text Embeddings v2 or similar efficient models often provide excellent performance at a fraction of the cost.

3. **Batch your requests**: When generating embeddings for a catalog, send texts in batches rather than one by one. This reduces network overhead and often improves throughput.

---

## Tomorrow's Teaser

Santa has the data, the safety checks, and the search. But now he faces a deeper challenge: remembering who these children actually *are*. Ten years of history, millions of behavior logs—how do you make an AI remember a childhood?

---

## Technical Specifications

### Input Files

- **toy_catalog.csv**: A CSV file containing a list of toys with descriptions, categories, and other metadata.
- **vague_wishes.json** (Optional/Generated): A list of vague wishes to test against the catalog (e.g., "something red that goes fast", "a toy for building things").

### Expected Output

- **semantic_matches.json**: A JSON file containing the vague wishes and their top 3 semantic matches from the catalog, including similarity scores.

### Output Format Example

```json
[
  {
    "query": "something red that goes fast",
    "matches": [
      {
        "product_name": "Turbo Fire Truck",
        "description": "A bright red fire engine with working sirens and high-speed wheels.",
        "score": 0.89
      },
      {
        "product_name": "Lightning Racer",
        "description": "Red sports car, built for speed.",
        "score": 0.87
      }
    ]
  }
]
```

### Getting Started

1. **Load the catalog**: Read `input/toy_catalog.csv` and prepare the text descriptions for embedding.
2. **Generate catalog embeddings**: Use Amazon Bedrock (Titan Text Embeddings v2) to create vectors for each product description.
3. **Store the vectors**: Keep them in memory (numpy array) or save to a file for this exercise.
4. **Process a query**: Take a vague wish (e.g., "something red that goes fast"), generate its embedding.
5. **Calculate similarity**: Compute cosine similarity between the query vector and all catalog vectors.
6. **Rank and return**: Sort by score and return the top matches.

### Prerequisites

- Completion of previous days
- Access to Amazon Bedrock (Titan Text Embeddings v2)
- Basic understanding of vectors (helpful but not strictly required—think of them as coordinate points)
- `numpy` or `scikit-learn` for cosine similarity (or write your own simple function)

### Concepts Covered

- Text Embeddings
- Vector Space Models
- Semantic Search vs. Keyword Search
- Cosine Similarity
- Dimensionality Reduction (conceptual)
