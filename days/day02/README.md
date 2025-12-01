# Day 2: Structure from Chaos

## Story

The workshop was still silent, but now it felt different—less like abandonment and more like anticipation.

Santa sat at his desk with the Apprentice beside him, both staring at the screen. They'd spent the morning processing letters through the summarization prompt, and the results were... good. Clean. Readable. But as the summaries accumulated, Santa began to feel a new kind of overwhelm.

"Look at this," he said, gesturing at the screen. "I have a hundred summaries now. But they're all different. One says 'Marcus wants a gaming setup.' Another says 'Sarah's wish is a bicycle, red, with training wheels.' A third says 'Tommy requested a chemistry set but his parents are concerned about safety.'"

The Apprentice leaned forward. "What's the problem?"

"The problem," Santa said slowly, "is that I can't do anything with this. I can't search it. I can't organize it. I can't cross-reference it with my Nice List. I can't even tell you how many children want bicycles versus gaming setups. It's all just... text."

The Apprentice was quiet for a moment, then smiled. "What if we made it structured?"

"Structured how?"

"JSON," the Apprentice said. "We take each summary and extract the key information into a consistent format. Every letter becomes a record with the same fields: name, age, address, wishlist, special notes. Then it becomes data. Then we can actually work with it."

Santa felt something click into place. "You mean... we teach the model to extract information?"

"Exactly. We give it a template. We show it what we want. We ask it to fill in the blanks."

They spent the next hour crafting a new prompt. This one was more complex—it needed to extract multiple pieces of information and format them precisely. They tested it on a few letters, refining it each time. The model learned. It began to understand the pattern.

By afternoon, they had it working.

"Look," the Apprentice said, showing Santa the output. "Every letter is now a JSON object. Name, age, address, wishlist items, any special notes. All consistent. All machine-readable."

Santa scrolled through the data, watching the chaos transform into order. Marcus became a record. Sarah became a record. Tommy became a record. Thousands of individual wishes, now organized into a structure that could be searched, sorted, analyzed.

"This is..." Santa paused, searching for the word. "This is beautiful."

"This is just the beginning," the Apprentice said. "Now that we have structured data, we can do real work. We can match wishes to inventory. We can check behavior history. We can make decisions."

Santa looked at the Apprentice with something like awe. "You're saying that by teaching the model to extract information in a consistent way, we've transformed chaos into something we can actually work with?"

"That's exactly what I'm saying."

Santa stood and walked to the window, looking out at the silent workshop. Tomorrow, he thought. Tomorrow we start filling those shelves again. But first, we need to understand what we're working with. First, we need structure.

"Show me how to do this at scale," he said. "Show me how to process thousands of letters this way."

The Apprentice was already typing. "Let's start with twelve. Then one hundred twenty. Then twelve hundred. We'll build up gradually, making sure the extraction stays clean and consistent."

As the afternoon light faded, Santa watched the letters transform. Chaos became data. Noise became signal. And somewhere in that transformation, the impossible began to feel possible again.

---

![Day 2 Image](images/day02.png)

## Learning Goal

**Entity Extraction and JSON Formatting**

Today you'll learn how to use foundation models to extract structured information from unstructured text. This is called *entity extraction*—identifying specific pieces of information (name, age, address, wishlist) and pulling them out into a consistent format. JSON (JavaScript Object Notation) is a standard format for storing structured data that computers can easily read and process. By combining prompt engineering with structured output formatting, you can transform messy real-world text into clean, machine-readable data. This is a critical skill in GenAI workflows: the ability to take human-written input and convert it into data that systems can work with. In Project Sleigh-Ride, this lets Santa convert thousands of individual letters into a database he can search, sort, and analyze.

---

## Participant Challenge

Today, you'll practice entity extraction using the materials provided for this day. You'll take a batch of letters (each already summarized from Day 1) and craft a prompt that teaches a foundation model to extract key information (child's name, age, address, wishlist items, special notes) and format it as JSON. The goal is to demonstrate that with the right prompt and output format specification, you can reliably convert unstructured text into structured data that can be processed by other systems.

---

## Cost-Saving Tips

1. **Use consistent JSON schemas**: Define your output structure once and reuse it for all letters. This reduces token usage because the model learns the pattern and doesn't need to re-explain it for each input.

2. **Batch similar requests together**: Process multiple letters with the same prompt in a single API call when possible. Batching reduces overhead and can be more cost-effective than individual requests.

3. **Validate output format early**: Test your extraction prompt on 5-10 letters before scaling to thousands. A small mistake in your prompt can cause expensive re-processing of large batches.

4. **Request only necessary fields**: Don't ask the model to extract information you won't use. Each field adds tokens to the output. If you don't need "favorite color," don't ask for it.

5. **Use structured output modes**: Some models support "structured output" modes that enforce JSON format without requiring verbose prompting. This can reduce token usage by 10-20%.

---

## Tomorrow's Teaser

Tomorrow, Santa discovers that structured data isn't enough—the children deserve personalization. And that means pictures.

---

## Technical Specifications

### Input Files

- **letters_batch_01.txt**: A file containing 12 distinct letters from children across Canada. Letters are separated by clear delimiters (`--- START LETTER ---` and `--- END LETTER ---`). Each letter includes the child's name, address, date, and their Christmas wishes written in various styles (from formal to very casual).

**Preview of letters_batch_01.txt:**
```
--- START LETTER ---
From: Lucas Walsh
Address: 8727 Eaton Mount, Brampton, Ontario, N2D 0E1, Canada
Date: 2024-11-17

Yo Santa!

Lucas checking in from Brampton, Ontario. This year's been wild, but I've kept it cool. 
I'm hyped about maybe getting an electric scooter. And, if you're feeling extra jolly, a virtual reality headset would blow my mind!

Stay frosty!
Lucas
--- END LETTER ---

--- START LETTER ---
From: Donna Jones
Address: 3727 Karen Prairie Apt. 100, Sydney, Nova Scotia, B8Q 3E5, Canada
Date: 2024-12-03

Hi Santa!

Donna here, waving from Sydney, Nova Scotia. I've been trying my best to be good (most of the time).
I'm really hoping to find an Our Generation Siberian Husky Plush under the tree. And if there's room in your bag, a video game would be amazing!

Thanks for being awesome!
Donna
--- END LETTER ---

[... 10 more letters with similar structure]
```

**Note**: The letters vary in tone from casual ("Yo Santa!") to formal ("Dear Santa Claus"). Some children provide complete addresses while others may omit certain details. **None of the letters explicitly mention the child's age**, so this field should be set to `null` when not available.

### Expected Output

- **extracted_letters.json**: A JSON file containing an array of letter objects, each with the following structure:

```json
{
  "letters": [
    {
      "child_name": "string",
      "age": "integer or null",
      "address": {
        "street": "string or null",
        "city": "string or null",
        "province": "string or null",
        "postal_code": "string or null"
      },
      "wishlist": [
        "string (individual wish items)"
      ],
      "special_notes": "string or null"
    }
  ]
}
```

### Output Format Example

```json
{
  "letters": [
    {
      "child_name": "Marcus",
      "age": 14,
      "address": {
        "street": "123 Maple Street",
        "city": "Toronto",
        "province": "Ontario",
        "postal_code": "M5V 3A8"
      },
      "wishlist": [
        "Gaming graphics card",
        "Mechanical keyboard",
        "Gaming mouse"
      ],
      "special_notes": "Interested in competitive gaming"
    },
    {
      "child_name": "Sarah",
      "age": 7,
      "address": {
        "street": null,
        "city": "Vancouver",
        "province": "British Columbia",
        "postal_code": null
      },
      "wishlist": [
        "Red bicycle with training wheels",
        "Bicycle helmet"
      ],
      "special_notes": "Learning to ride"
    }
  ]
}
```

### Validation Criteria

- Output file is valid JSON (can be parsed without errors using Python's `json.load()` or an online validator)
- All required fields are present for each letter (`child_name`, `age`, `address`, `wishlist`, `special_notes`)
- Wishlist items are individual strings in an array (not comma-separated in a single string)
- Age is an integer or null (not a string) - **Note: All letters in this batch lack explicit age information, so null is expected**
- Address fields follow the nested structure with `street`, `city`, `province`, and `postal_code`
- Address sub-fields are null if not provided in the original letter (e.g., if apartment number is missing)
- No information from the original letters is lost (all wishes and context are captured)
- All 12 letters from the input batch are represented in the output
- `special_notes` captures relevant context about the child's behavior or circumstances mentioned in the letter
- Consistent formatting across all letter objects (same field names, same data types)

### Getting Started

1. **Review the starter script**: Check `output/day02_structure_from_chaos.py` for a template structure with TODO markers
2. **Verify Bedrock access**: Ensure you have Amazon Bedrock enabled in your AWS account (see `setup/bedrock_setup_guide.md` if needed)
3. **Choose your model**: The example uses Claude 3 Sonnet, but you can use any text model available in Bedrock that supports structured output
4. **Understand the input format**: Review `input/letters_batch_01.txt` to see the delimiter structure and letter variations
5. **Design your JSON schema**: Before prompting, clearly define the exact structure you want (refer to the Expected Output section)
6. **Craft your extraction prompt**: The key to success is writing a prompt that:
   - Specifies the exact JSON schema you want
   - Instructs the model to extract all letters from the batch
   - Handles missing information gracefully (use null for absent fields)
   - Maintains consistency across all extractions
7. **Test and iterate**: Start by processing the batch and checking if the output matches the expected format

**Recommended Approach:**
- Read through 2-3 sample letters to understand what information is available
- Design your prompt to explicitly request JSON output with the specified schema
- Include instructions for handling missing data (e.g., "if age is not mentioned, set to null")
- Consider using the model's structured output capabilities if available
- Validate your JSON output using Python's `json.load()` to catch formatting errors
- Check that all 12 letters are present and no information is lost

**Prompt Engineering Tips for Entity Extraction:**
- Be explicit about the JSON structure in your prompt (you can include the schema as an example)
- Instruct the model to process ALL letters in the batch, not just the first one
- Specify how to handle missing fields ("use null if not present")
- Request that wishlist items be separated into individual array elements
- Ask for special_notes to capture behavioral context ("I've been good", "trying my best", etc.)

### Prerequisites

- Completion of Day 1 (understanding of prompt engineering and Bedrock basics)
- Basic familiarity with JSON structure and syntax
- Understanding of how to validate JSON (using online validators or Python's json module)
- Access to the same AWS Bedrock setup from Day 1
- Familiarity with parsing delimited text files

### Concepts Covered

- Entity extraction from unstructured text
- JSON structure and formatting
- Prompt design for structured output
- Data validation and quality assurance
- Batch processing of similar requests
- Handling missing or incomplete information (null values)
- Scaling extraction from individual letters to batches
