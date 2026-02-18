# 📅 25-Day Challenge Structure

**Complete guide to the daily challenges**

---

## Welcome to Project Sleigh-Ride

This folder contains all 25 days of the Sleigh-Ride Cloud Chronicles challenge. Each day is a self-contained learning unit with:
- 📖 **Story**: Narrative context for the technical challenge
- 🎯 **Learning Goal**: What you'll learn and why it matters
- 📁 **Input Files**: Sample data to process
- 🎬 **Expected Output**: Reference solutions showing what success looks like
- 💡 **Tips**: Cost-saving and practical advice

---

## 📂 Folder Structure

Each day follows the same structure:

```
dayXX/
├── README.md                 # Day's story, goal, and challenge
├── input/                    # Sample input files to process
│   ├── file_1.txt
│   ├── file_2.json
│   └── ...
├── output/                   # Expected output templates & starter scripts
│   ├── dayXX_solution.py     # Starter code template
│   ├── expected_output.json  # Reference solution format
│   └── ...
└── images/                   # Visual assets for the day
    ├── dayXX.png
    └── ...
```

---

## 🗺️ The 25-Day Journey

### **Phase 1: Digitization & Basic Understanding** (Days 1-6)
**[Read Story: Chapter I - The Arrival of the Wayfarer](../STORY.md)**

Foundation skills for processing and understanding text.

| Day | Challenge | Technical Focus | Story Element |
|-----|-----------|-----------------|--------------|
| **1** | [The First Digital Letter](day01/README.md) | Prompt Engineering | Chaos → Signal |
| **2** | [Structure from Chaos](day02/README.md) | Entity Extraction & JSON | Data Organization |
| **3** | [The Picture Perfect Card](day03/README.md) | Image Generation | Visual Magic |
| **4** | [The Validation Gate](day04/README.md) | Safety Guardrails | Adding Conscience |
| **5** | [The 10-Page Manifesto](day05/README.md) | Token Chunking | Processing Limits |
| **6** | [The Vague Wish](day06/README.md) | Semantic Search | Understanding Intent |

**What You'll Build**: A complete data processing pipeline that transforms chaotic input into clean, structured, safe data.

---

### **Phase 2: Knowledge & Memory** (Days 7-12)
**[Read Story: Chapter II - The Great Well of Memory](../STORY.md)**

Building systems that understand context and make wise decisions.

| Day | Challenge | Technical Focus | Story Element |
|-----|-----------|-----------------|--------------|
| **7** | [The Nice List Vector Store](day07/README.md) | Vector Stores & RAG | Building Memory |
| **8** | [Retrieval Augmented Christmas](day08/README.md) | RAG Pipelines | Using Memory |
| **9** | [Complex Context Reconstruction](day09/README.md) | Data Fusion | Solving Mysteries |
| **10** | [Rudy's Memory (Short Term)](day10/README.md) | Conversation Memory | Remembering Context |
| **11** | [The Moral Compass](day11/README.md) | Ethical Reasoning | Nuanced Judgment |
| **12** | [The Priority Queue](day12/README.md) | Prioritization | Triage & Urgency |

**What You'll Build**: Knowledge systems that ground decisions in historical context and make ethically sound choices.

---

### **Phase 3: Agents & Tools** (Days 13-18)
**[Read Story: Chapter III - The Manifestation of Spirits](../STORY.md)**

Creating autonomous agents that can execute real actions.

| Day | Challenge | Technical Focus | Story Element |
|-----|-----------|-----------------|--------------|
| **13** | [Enter Rudy (The Orchestrator)](day13/README.md) | Agent Personas | Planner Agent |
| **14** | [Enter Elfie (The Tool User)](day14/README.md) | Tool Integration | Executor Agent |
| **15** | [Agent Collaboration](day15/README.md) | Multi-Agent Coordination | Learning to Work Together |
| **16** | [The API Call (MCP)](day16/README.md) | API Integration | Reaching External Systems |
| **17** | [The Safety Filter](day17/README.md) | Agent Guardrails | Safety Constraints |
| **18** | [The Brain of the Operation](day18/README.md) | Agent Core | Shared Cognition |

**What You'll Build**: A multi-agent system where specialized agents work together with shared memory and coordinated decision-making.

---

### **Phase 4: Coordination, Control & Trust** (Days 19-23)
**[Read Story: Chapter IV - The Heartbeat of the Cloud](../STORY.md)**

Mature systems that operate reliably and respect human oversight.

| Day | Challenge | Technical Focus | Story Element |
|-----|-----------|-----------------|--------------|
| **19** | [Planning Without Pipelines](day19/README.md) | Dynamic Planning | Reasoning over Scripts |
| **20** | [Context Sharing & Memory Optimization](day20/README.md) | Caching & Optimization | Efficiency |
| **21** | [Multimodal Consistency](day21/README.md) | State Synchronization | Single Source of Truth |
| **22** | [Human-in-the-Loop as First-Class Agent](day22/README.md) | HITL Escalation | Respecting Human Judgment |
| **23** | [The Executive Briefing](day23/README.md) | Summarization & Reporting | Management Overview |

**What You'll Build**: A production-ready system that operates efficiently, maintains consistency, and respects human oversight.

---

### **Phase 5: Grand Finale** (Days 24-25)
**[Read Story: Chapter V - The Final Flight & Epilogue](../STORY.md)**

Proving the system works at scale with full explainability.

| Day | Challenge | Technical Focus | Story Element |
|-----|-----------|-----------------|--------------|
| **24** | [Why Did You Buy Coal? (Explainability)](day24/README.md) | Decision Tracing | Accountability |
| **25** | [The Night Before Christmas (Scale)](day25/README.md) | Multi-Agent Orchestration | Ultimate Test |

**What You'll Build**: Full system validation with 43,492+ cases processed with perfect accuracy and explainability.

---

## 🚀 How to Use This Folder

### Starting a Day

**Option 1: Using Makefile (Recommended)**
```bash
# Show the task for today (e.g., Day 1)
make day01

# This displays:
# - Story section
# - Learning goal
# - Input files available
# - Expected output format
```

**Option 2: Direct Navigation**
```bash
# Navigate to a day
cd days/day01

# Read the challenge
cat README.md

# See what files you need
ls input/

# See what output format is expected
ls output/
```

**Option 3: Web Browser**
- Open `days/dayXX/README.md` directly in your editor or GitHub
- Click links to navigate between days and story

---

## 📖 Understanding Each Day's README

Every day's README includes:

### 1. **Story Section** (Story from narrative)
```markdown
## Story

[Narrative context from the larger story...]
This explains WHY the technical challenge exists.
```

### 2. **Learning Goal** (What you'll learn)
```markdown
## Learning Goal

[Concept explanation...]
This explains WHAT you're learning and WHY it matters.
```

### 3. **Participant Challenge** (What to do)
```markdown
## Participant Challenge

You will:
1. [Task 1]
2. [Task 2]
3. [Task 3]
```

### 4. **Cost-Saving Tips** (Practical advice)
```markdown
## Cost-Saving Tips

- Tip 1: ...
- Tip 2: ...
```

### 5. **Technical Specifications** (Detailed requirements)
```markdown
## Technical Specifications

### Input Files
[Description of files in input/]

### Expected Output
[Description of files to create in output/]
```

---

## 💡 Working on a Challenge

### Step 1: Read the Story
Start by reading the day's story section. This explains the narrative context and motivation.

### Step 2: Understand the Goal
Read the "Learning Goal" to understand what concept you're learning and why.

### Step 3: Check Input Files
Look in `input/` to see what data you'll be working with.

### Step 4: Study Expected Output
Look in `output/` to see what success looks like.

### Step 5: Write Your Solution
Write code to transform input → expected output.

### Step 6: Test & Iterate
Run your code, compare with expected output, refine.

### Step 7: Submit via PR
When done, commit your solution and open a pull request.

---

## 📊 Challenge Progression

### Difficulty Curve
Each phase builds on previous ones:

```
Phase 1 (Basic)
  ↓ Simple text processing
Phase 2 (Intermediate)
  ↓ Context-aware systems
Phase 3 (Advanced)
  ↓ Multi-agent coordination
Phase 4 (Expert)
  ↓ Optimization & control
Phase 5 (Master)
  ↓ Scale & explainability
```

### Time Estimates
- **Phase 1** (Days 1-6): 1-2 hours per day
- **Phase 2** (Days 7-12): 2-3 hours per day
- **Phase 3** (Days 13-18): 3-4 hours per day
- **Phase 4** (Days 19-23): 3-4 hours per day
- **Phase 5** (Days 24-25): 4-5 hours per day

(Estimates vary based on experience and approach)

---

## 🔗 Navigation

### Within Days
- **Next Day**: `cd ../dayXX/` or `make dayXX`
- **Previous Day**: `cd ../day(XX-1)/` or `make day(XX-1)`
- **Jump to Day X**: `make dayXX`

### Related Content
- **Full Story**: [STORY.md](../STORY.md)
- **Main README**: [README.md](../README.md)
- **Setup Guide**: [setup/](../setup/)
- **Datasets**: [datasets/](../datasets/)

### GitHub Navigation
- Click on `day01`, `day02`, etc. to navigate between days
- Click on "STORY.md" to read the full narrative
- Click on "README.md" to return to main project overview

---

## 💻 Template Workflow

Here's a typical workflow for completing a day:

```bash
# 1. Navigate to the day
cd days/dayXX

# 2. Read the challenge
cat README.md

# 3. Examine input files
ls input/
cat input/sample_file.txt

# 4. Examine expected output
ls output/
cat output/expected_output.json

# 5. Write your solution
python your_solution.py

# 6. Test your output
diff your_output.json output/expected_output.json

# 7. When working correctly, commit
cd ../..
git add days/dayXX/output/your_solution.py
git commit -m "Complete Day XX: Challenge Title"
```

---

## 🎯 Success Criteria

For each day, you're successful when:

✅ You understand the story context
✅ You understand the learning goal
✅ You can explain why the technical concept matters
✅ Your input files are processed correctly
✅ Your output matches (or exceeds) the expected format
✅ Your code is documented and reproducible
✅ You can explain your solution to someone else

---

## 🤔 Common Questions

**Q: What if I don't complete a day?**
A: That's okay! Days are designed to stand alone. You can skip ahead or revisit later.

**Q: Can I use different tools/languages?**
A: Absolutely! The challenges are language-agnostic. Use Python, Go, Rust, whatever you prefer.

**Q: How do I know if my solution is correct?**
A: Compare your output with the expected output in `output/`. The format should match.

**Q: Can I see other people's solutions?**
A: Check pull requests on GitHub to see how others approached challenges.

**Q: What if I get stuck?**
A: 1. Re-read the story (often contains hints), 2. Check the learning goal explanation, 3. Examine the expected output carefully, 4. Ask in GitHub discussions.

---

## 🔍 Quick Reference: Find a Specific Day

**Days 1-6**: Phase 1 - Digitization
- Day 1: Prompt engineering
- Day 2: Structuring data
- Day 3: Image generation
- Day 4: Safety guardrails
- Day 5: Token chunking
- Day 6: Semantic search

**Days 7-12**: Phase 2 - Knowledge & Memory
- Day 7: Vector stores
- Day 8: RAG pipelines
- Day 9: Data fusion
- Day 10: Conversation memory
- Day 11: Ethical reasoning
- Day 12: Prioritization

**Days 13-18**: Phase 3 - Agents & Tools
- Day 13: Agent personas
- Day 14: Tool integration
- Day 15: Agent coordination
- Day 16: API integration
- Day 17: Safety guardrails
- Day 18: Agent Core

**Days 19-23**: Phase 4 - Coordination & Trust
- Day 19: Dynamic planning
- Day 20: Memory optimization
- Day 21: Multimodal consistency
- Day 22: Human-in-the-loop
- Day 23: Executive reporting

**Days 24-25**: Phase 5 - Grand Finale
- Day 24: Explainability
- Day 25: Scale testing

---

## 📚 Learning Resources

Within This Project:
- **STORY.md**: Full narrative with character development
- **README.md**: Technical overview and setup
- **setup/**: Installation and configuration guides
- **datasets/**: Guide to available data

External Resources:
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Prompt Engineering Best Practices](https://www.anthropic.com/research/constitutional-ai)
- [Multi-Agent Systems](https://www.anthropic.com/research/long-context-language-models)

---

## 🎄 Final Thoughts

You're on a 25-day journey. Each day builds toward something larger. Pay attention to:

- **The Story**: It contains wisdom and guidance
- **The Progression**: Each phase is designed to scaffold learning
- **Your Growth**: You'll feel the difference between Day 1 and Day 25
- **The Mission**: Ultimately, you're helping Santa save Christmas 🎅

---

**Ready to begin? Start with [Day 1: The First Digital Letter](day01/README.md)**

*"The North Pole Cloud Apprentice. The story begins now."* ❄️✨
