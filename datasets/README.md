# 📊 Datasets - Sleigh-Ride Cloud Chronicles

**Shared data files used across the 25-day challenge**

---

## Overview

This folder contains all the shared datasets used throughout the 25-day challenge. These files provide realistic, curated data that grounds the technical exercises in a believable North Pole scenario.

**Total Size**: ~51 MB (mostly synthetic PDF letters)
**Purpose**: Give participants real data to work with without requiring external services

---

## 📂 Folder Structure

### `/letters/` - Synthetic Letter Collection
**~47 MB of synthetic PDF/text files**

Contains 5,000+ simulated children's letters in various formats:
- **Format**: PDF, TXT
- **Content**: Letters from children requesting gifts, describing behavior, sharing stories
- **Realism**: Generated with varied handwriting styles, ages, backgrounds
- **Used in**: Days 1-6 (processing), Days 7-12 (understanding context), Days 13-25 (agent handling)

**Key Files**:
- `letter_001.txt` - Lucas's chaotic letter (Day 1 example)
- `letters_batch_01.txt` - Batch of 10 letters (Day 2)
- `letter_tammy.txt` - Tammy's letter for RAG (Day 8)
- `letter_complex_wish.txt` - Complex multi-step request (Day 15)
- `letter_pony.txt` - The pony request (Day 22)

### `/logs/` - Behavior Logs & Activity Records
**Agent traces, API logs, behavior history**

Contains structured records of children's activities and behaviors:
- **behavior_logs.json** - 10 years of recorded behavior (nice/naughty actions)
- **activity_log.json** - Timestamped activity records
- **chat_history.json** - Sample conversation logs (Day 10)
- **incident_fragment.txt** - Fragmented incident report for detective work (Day 9)

**Used in**: Days 7-12 (knowledge/memory), Days 13-25 (agent decision-making)

### `/behavior/` - Behavioral Data
Detailed behavioral records for individual children:
- Nice/Naughty classifications
- Action timestamps and descriptions
- Contextual information for nuanced judgment

### `/catalogs/` - Gift & Inventory Catalogs
**Product databases and inventory**

- **toy_catalog.csv** - Master catalog of available toys with prices, stock levels
- **inventory_db.json** - Real-time inventory database schema
- **product_search_requirements.txt** - API specifications for inventory search

**Used in**: Days 6 (semantic search), Days 14-16 (tool usage), Days 20+ (inventory checks)

### `/inventory/` - Stock Management Data
Detailed inventory tracking:
- Stock levels by location (Warehouse A, B, C)
- Item availability and pricing
- Fulfillment constraints

**Used in**: Days 14-23 (agent tool calls)

### `/addresses/` - Geographic & Mailing Data
**Location information for delivery**

- Address databases for mail routing
- Geographic coordinates for logistics
- Regional categorization

### `/raw/` - Raw Unprocessed Data
**Source data before processing**

- Original letters before cleanup
- Unstructured logs
- Raw API responses

---

## 🎯 How to Use These Datasets

### Phase 1: Digitization (Days 1-6)
- Use `/letters/` files as input
- Process with prompt engineering
- Output cleaned, structured data

**Example**:
```bash
# Day 1: Process a messy letter
input: datasets/letters/letter_001.txt
output: days/day01/output/letter_001_clean.md
```

### Phase 2: Knowledge & Memory (Days 7-12)
- Use `/behavior/` and `/logs/` files
- Build embeddings from behavior records
- Create vector stores for semantic search

**Example**:
```bash
# Day 7: Index behavior logs
input: datasets/logs/behavior_logs.json
output: days/day07/output/vector_store.json
```

### Phase 3-5: Agents & Orchestration (Days 13-25)
- Use `/catalogs/` and `/inventory/` for tool integration
- Use `/letters/` for real cases to process
- Use all data types for complex multi-source challenges

**Example**:
```bash
# Day 14: Tool integration - check inventory
input: datasets/inventory/inventory_db.json
tool: get_inventory_item("Red Racing Bike")
output: days/day14/output/inventory_result.json
```

---

## 📋 Dataset Specifications

### Letter Files (letters/)
- **Format**: TXT or PDF
- **Encoding**: UTF-8
- **Size**: 1-50 KB per file (except batches)
- **Content**: Unstructured, realistic childhood letters with:
  - Emojis and text speak
  - Handwriting variations
  - AI-generated suggestions
  - Personal stories and context

### Behavior Logs (logs/)
- **Format**: JSON
- **Schema**: `{id, name, date, action, category, details}`
- **Content**: 10+ years of historical behavior
- **Realistic**: Mix of nice and questionable behaviors

### Inventory (inventory/)
- **Format**: JSON or CSV
- **Schema**: `{item_id, name, price, stock, warehouse, category}`
- **Realistic**: Limited stock, pricing variations, location constraints

### Addresses (addresses/)
- **Format**: CSV or JSON
- **Schema**: `{id, name, street, city, state, country, postal_code}`
- **Geographic**: Global distribution of children

---

## ⚠️ Important Notes

### Data Realism
All datasets are **synthetic but realistic**:
- Generated with attention to detail
- Include edge cases and anomalies
- Represent real-world messiness
- Not production data (safe to experiment with)

### Data Freshness
- Datasets are static and don't change between runs
- Safe for reproducible testing
- Ideal for learning (consistent input → consistent output)

### Data Privacy
- All data is **completely fictional**
- No real children's information
- Safe for public code repositories
- Can be shared freely in pull requests

### Data Scale
- **Small enough**: To process locally without huge resources
- **Large enough**: To practice real-world patterns (5000+ records)
- **Representative**: Edge cases included for robust solutions

---

## 🔗 Related Documentation

- **[Main README](../README.md)** - Project overview and setup
- **[Story (STORY.md)](../STORY.md)** - Narrative context for datasets
- **[Individual Days](../days/)** - Each day's specific dataset usage
- **[Setup Guide](../setup/)** - Environment configuration

---

## 📊 Data Usage by Day

| Phase | Days | Primary Datasets | Purpose |
|-------|------|-----------------|---------|
| **Digitization** | 1-6 | `/letters/` | Processing & structuring |
| **Knowledge** | 7-12 | `/logs/`, `/behavior/` | Building memory systems |
| **Agents** | 13-18 | `/catalogs/`, `/inventory/` | Tool integration |
| **Coordination** | 19-23 | All | Complex orchestration |
| **Finale** | 24-25 | All | Scale testing & finale |

---

## 🚀 Getting Started with Datasets

### 1. Explore Available Data
```bash
ls -la datasets/
ls -la datasets/letters/ | head -20
```

### 2. View Sample Letter
```bash
cat datasets/letters/letter_001.txt
```

### 3. Inspect Behavior Logs
```bash
cat datasets/logs/behavior_logs.json | head -50
```

### 4. Check Inventory Schema
```bash
cat datasets/inventory/inventory_db.json
```

---

## 💡 Tips for Working with Datasets

1. **Start Small**: Test your code with single files before batch processing
2. **Understand Structure**: Read sample files before writing processing code
3. **Handle Edge Cases**: Datasets include messy, ambiguous, incomplete data
4. **Preserve Originals**: Don't modify files in `/datasets/` directly
5. **Document Your Work**: Keep notes on how you used each dataset
6. **Share Insights**: PR comments about dataset patterns help others learn

---

## Questions?

- **How does this data relate to the story?** Read [STORY.md](../STORY.md)
- **Which dataset do I need for Day X?** Check the day's README in `/days/dayXX/`
- **Can I add my own data?** Yes! Create a new subfolder and document it
- **Is this data realistic?** Yes, it's synthetic but carefully curated

---

**Happy exploring! These datasets are designed to make learning feel real.** 📚✨

*Remember: The data tells a story. Pay attention to patterns, contradictions, and details — they matter in the North Pole.*
