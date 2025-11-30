# Day 1: The First Digital Letter

## Story

The North Pole had never been silent before.

Santa stood in his office, surrounded by the accumulated weight of centuries—leather-bound ledgers, quills worn smooth by centuries of handwriting, the faint scent of cinnamon and pine that had always meant home. But today, the workshop beyond the frosted windows was empty. The conveyor belts had stopped. The toy-making machines sat dormant like sleeping giants. And the letters—oh, the letters—were piling up in drifts across every surface.

It had started three weeks ago. The Elves had gone on strike, something about dental insurance for candy-cane-related injuries. The Reindeer had simply vanished, last spotted boarding a flight to Ibiza with sunglasses and a travel brochure. Santa had laughed at first. Surely they'd return. Surely this was temporary.

But December 1st had arrived, and the letters kept coming.

Millions of them. Digital now, mostly—uploaded to something called an "S3 bucket" by tech-savvy children who'd never known a world without the internet. The first one sat on his screen, a glowing rectangle of chaos: emojis, slang, fragments of sentences interrupted by what appeared to be AI-generated nonsense. A child named Lucas from Brampton had written about wanting "an electric scooter" and "a virtual reality headset," but the text was buried under layers of autocorrect mishaps, cat-induced keyboard smashing, and suggestions from what Lucas called his "smart AI helper app" that had added bizarre phrases about manifesting "inner snowman energy."

Santa rubbed his temples. He was 1,752 years old, and he'd never felt more lost.

That's when the door opened.

"You look like you could use some help," said a voice—young, steady, with the kind of practical optimism that only comes from someone who hasn't yet learned to be afraid of impossible things.

Santa looked up to see a figure in the doorway, silhouetted against the workshop lights. The North Pole Cloud Apprentice. He'd sent out a desperate call to the world's greatest logistics company—Amazon—and they'd sent him this: a human partner, someone who understood both the old magic of Christmas and the new magic of clouds and algorithms.

"I don't even know where to start," Santa admitted, gesturing at the screen. "This letter—I can't tell what the child actually wants. There's too much noise."

The Apprentice stepped closer, studying the glowing text. "What if we taught the AI to listen better? To filter out the noise and find what matters?"

"How?" Santa asked, though something in his chest had already begun to hope.

"We ask it the right questions," the Apprentice said simply. "We tell it what we're looking for. We teach it to summarize—to find the signal in all this static."

Santa leaned back in his chair, considering this. For centuries, he'd relied on instinct, on the accumulated wisdom of ages. But instinct couldn't process millions of letters. Instinct couldn't scale. Maybe, he thought, this new world had something to teach him after all.

"Show me," he said.

The Apprentice pulled up a chair and began typing, crafting a prompt with the precision of someone writing a spell. "We tell the model: 'This is a letter from a child. Extract the core wish, remove any AI-generated noise, emojis, and irrelevant text, and give us a clean summary.' Simple. Clear. Focused."

They sent the prompt to Amazon Bedrock, and the model responded within seconds. The noise fell away. What remained was pure: Lucas wanted an electric scooter and a VR headset. That was all. That was everything.

Santa felt something shift inside him—not quite hope, but its cousin. The beginning of possibility.

"Tomorrow," he said quietly, "we'll do this again. And again. Until we've read them all."

The Apprentice smiled. "And then?"

"Then," Santa said, looking out at the silent workshop, "we rebuild Christmas."

![Day 1: The First Digital Letter](images/day01.png)

---

## Learning Goal

**Basic Prompt Engineering and Text Summarization**

Today you'll learn how to use foundation models to clean and summarize unstructured text. The core concept is *prompt engineering*—the art of asking an AI model the right question in the right way to get useful answers. When you craft a clear, focused prompt that specifies what you want (extract the core wish, remove noise), the model can process messy, real-world data and produce clean, actionable results. This is the foundation of all GenAI work: understanding that how you ask matters as much as what you ask. In Project Sleigh-Ride, this skill lets Santa transform millions of chaotic letters into readable summaries, making the impossible task of reading every letter suddenly manageable.

---

## Participant Challenge

Today, you'll practice prompt engineering using the materials provided for this day. You'll take a messy, real-world letter filled with emojis, slang, and AI-generated noise, and craft a prompt that teaches a foundation model to extract the core message and produce a clean summary. The goal is to demonstrate that with the right prompt, even chaotic input can become clear, structured output—a skill you'll use throughout Project Sleigh-Ride.

---

## Cost-Saving Tips

1. **Be specific in your prompt**: Instead of "summarize this," try "extract the child's main wish and remove any AI-generated text." Specificity reduces token usage by preventing the model from generating unnecessary elaboration.

2. **Use few-shot examples sparingly**: One or two examples in your prompt can dramatically improve output quality without doubling your token count. More examples don't always mean better results.

3. **Reuse prompts across similar inputs**: If you're processing thousands of letters, use the same well-crafted prompt for all of them rather than tweaking each one. Consistency saves tokens and improves batch processing efficiency.

4. **Request concise output formats**: Ask for bullet points or short paragraphs instead of long prose. "Summarize in 2-3 sentences" costs less than "write a detailed summary."

5. **Test on a small batch first**: Before processing 1 million letters, validate your prompt on 10-20 examples. This prevents expensive mistakes at scale.

---

## Tomorrow's Teaser

Tomorrow, Santa realizes that summaries alone aren't enough—he needs *structure*. The letters must become data.

---

## Technical Specifications

### Input Files

- **letter_001.txt**: A single letter from a child, containing emojis, slang, and AI-generated noise mixed with the actual wish.

**Preview of letter_001.txt:**
```
YO Saaaaaanta!!! 🎅🔥🔥 What's up my red-suit legend??

It's ya boy LUCAS WALSH from BRAMPTON (Ontario, Canada, you know, near that giant parking lot everyone calls Toronto lol 😂).
Address is still the same btw: 8727 Eaton Mount, Brampton, N2D 0E1, pls don't mix it up again...

[Letter continues with emojis, slang, cat keyboard smashing, and AI-generated phrases like "manifest your inner snowman energy"]
```

The challenge is to extract the meaningful information (Lucas wants an electric scooter and VR headset) from all this noise.

### Expected Output

- **letter_001_clean.md**: A cleaned, summarized version of the letter containing:
  - Child's name (if provided)
  - Location (city, state/province, country if mentioned)
  - Date (when the letter was written or processed)
  - Core wish or request (1-2 sentences)
  - Any important context (age, location, special circumstances)
  - Notes section documenting what noise was removed
  - Removal of all AI-generated noise and irrelevant text

### Output Format Example

```markdown
# Letter Summary

**Child's Name:** Lucas Walsh  
**Location:** Brampton, Ontario, Canada  
**Date:** 2024-11-17  

**Core Wish:** Lucas is asking for an electric scooter and a virtual reality headset. He prefers a scooter that is fun but not too fast, and he is excited about VR games such as those involving dinosaurs or boxing.

**Context:**  
Lucas describes his year as hectic but says he has been trying his best. His cat frequently disrupts his typing, and he mentions autocorrect issues and a friend's AI app adding unnecessary emojis. He specifically asks Santa not to confuse his address again after last year's delivery mistake.

**Notes:**  
The original letter contained slang, jokes, repeated emojis, self-interruptions, and unrelated text caused by his cat and an AI writing assistant. These elements were removed to focus on the core request.
```

### Validation Criteria

- Output file is valid Markdown with proper formatting
- Summary includes all required fields: Name, Location, Date, Core Wish, Context, Notes
- Summary is concise but complete (typically 100-200 words total)
- All AI-generated noise, emojis, and irrelevant text has been removed
- Core wish is clearly stated and accurately reflects the child's actual request
- No information from the original letter is lost (only noise is removed)
- Context section captures relevant personal details mentioned in the letter
- Notes section documents what types of content were filtered out


### Getting Started

1. **Review the starter script**: Check `output/day01_process_letter.py` for a template structure
2. **Set up Bedrock access**: Ensure you have Amazon Bedrock enabled in your AWS account (see `setup/bedrock_setup_guide.md`)
3. **Choose your model**: The example uses Claude 3.5 Sonnet, but you can use any text model available in Bedrock
4. **Craft your prompt**: The key to success is writing a clear, specific prompt that tells the model exactly what to extract and what to ignore
5. **Test and iterate**: Start with the provided letter and refine your prompt until the output matches the expected format

**Recommended Approach:**
- Read the input letter first to understand what "noise" looks like
- Design your prompt to specifically address the types of noise you see (emojis, slang, AI-generated text, cat keyboard smashing)
- Ask the model to extract structured information (name, location, wishes) explicitly
- Request a specific output format (markdown with headers)

### Prerequisites

- Active AWS account with Amazon Bedrock access
- Access to Claude 3.5 Sonnet or similar foundation model
- Basic familiarity with the AWS console or Boto3 SDK
- Understanding of what a "prompt" is (a question or instruction you give to an AI model)

### Concepts Covered

- Foundation Models (FMs) and how to invoke them
- Prompt engineering basics
- Text summarization
- Noise filtering and data cleaning
- Token usage and cost optimization
