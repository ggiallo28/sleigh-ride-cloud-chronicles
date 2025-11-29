# 🎄 Sleigh-Ride Cloud Chronicles

**A 25-Day Cloud Engineering & AI Adventure**

---

## 📜 Prologue: *The Night the North Pole Fell Silent*

It is December 1st at the North Pole, and something has gone profoundly wrong.

The workshops, once alive with laughter and whirring gears, stand silent. Conveyor belts are frozen mid motion. Santa’s office is buried beneath mountains of unopened letters, each one a small voice hoping to be heard. The Elves have walked out, demanding fair dental care after centuries of candy cane casualties, and the Reindeer have escaped to Ibiza for a sun soaked, entirely unauthorized holiday.

For the first time in centuries, Santa stands truly alone.

He feels the weight of a world that still believes in him, even as everything around him collapses. And in that quiet, he realizes he has only one place left to turn: Amazon. Not for magic, but for the kind of infrastructure that can shoulder a miracle at scale.

Amazon cannot give him elves or reindeer, but it offers something new, something strange and powerful: the cloud. Tools that hum like distant northern lights. Systems that respond like invisible helpers. Models that listen, reason, and create.

In this moment of crisis, Santa makes a choice that will change Christmas forever.

He will reinvent himself.

Over the next 25 days, with millions of children waiting and time slipping like snow through gloved fingers, Santa will become the world’s first Generative AI Cloud Architect. He will build an autonomous Christmas engine using Amazon Bedrock, Lambda functions, vector databases, and AI agents unlike anything the North Pole has ever seen.

He calls it Project Sleigh Ride.

And though he begins this journey alone, he does not stay alone.

He has asked for your help, you, the one soul who still steps forward when others step away.

The North Pole Cloud Apprentice.

The story begins now.


---

## 🎅 Characters

### Santa Claus (Human-in-the-Loop)
The protagonist and final decision-maker. Once a master of traditional toy-making and logistics, Santa is now forced to become the world's first Generative AI Cloud Architect. He is warm, determined, occasionally overwhelmed, but fundamentally optimistic. Santa provides domain knowledge about children's behavior, approves budgets, and makes final decisions on edge cases. He learns alongside the participant, growing from skeptical about AI to becoming a confident orchestrator of autonomous systems.

### The North Pole Cloud Apprentice (You)
The participant and Santa's trusted partner throughout this journey. You learn cloud engineering and AI concepts alongside Santa, helping him solve each day's crisis. You write the code, deploy the infrastructure, and make the technical decisions that keep Project Sleigh-Ride moving forward. Your growth from novice to confident cloud architect mirrors the narrative arc of the challenge.

### Supporting Cast
- **Amazon Bedrock** – The magical AI engine powering Santa's solutions.
- **AWS Services** – The toolbox (Lambda, S3, DynamoDB, etc.) that Santa uses to build the system.

---

## 📖 What is Sleigh-Ride Cloud Chronicles?

Sleigh-Ride Cloud Chronicles is a narrative-driven cloud engineering challenge that unfolds over 25 days. Each day presents a new chapter in Santa's desperate journey to rebuild Christmas using generative AI and cloud infrastructure after his workshop falls into chaos.

Unlike traditional coding challenges, this project combines:
- **Immersive storytelling** with character development and emotional stakes
- **Real-world cloud architecture** using AWS services (Bedrock, Lambda, S3, DynamoDB)
- **Progressive skill building** from basic prompt engineering to multi-agent orchestration
- **Practical infrastructure-as-code** approaches to solve realistic problems

This is not a speed contest. It is a learning journey designed for engineers who want to build cloud AI systems while following a compelling narrative.

---

## 🎯 Who Should Participate?

This challenge is designed for:
- Cloud engineers learning generative AI capabilities
- AI practitioners exploring AWS infrastructure
- Developers wanting hands-on experience with multi-agent systems
- Anyone interested in RAG (Retrieval-Augmented Generation), embeddings, and agentic workflows
- Teams looking for collaborative learning exercises

**Prerequisites:**
- Basic Python programming knowledge
- An active AWS account with Bedrock access
- Familiarity with command-line tools
- Willingness to learn infrastructure-as-code principles

You do **not** need prior experience with AI/ML or advanced cloud architecture to start.

---

## 🚀 How It Works

### Daily Structure

Each day includes:
1. **Story Chapter** – A narrative scene advancing the plot and introducing the day's technical theme
2. **Learning Goal** – Conceptual explanation of the cloud/AI concept you'll implement
3. **Challenge Materials** – Input files and task descriptions in the `dayXX/` folders
4. **Expected Outputs** – Reference examples showing what success looks like
5. **Cost-Saving Tips** – Practical advice for managing AWS spend

### Your Mission

Each day, you will:
- Read the story chapter to understand the context
- Review the technical learning goal
- Implement your solution using the provided input files
- Generate the expected outputs
- Share your code and infrastructure definitions via pull request

---

## 📚 Learning Path Overview

### Phase 1: Digitization & Basic Understanding (Days 1-6)
Santa learns to process children's letters using basic prompt engineering, text summarization, entity extraction, and embeddings. Focus on the fundamentals of generative AI: prompt engineering, structuring unstructured data, and understanding semantic meaning. You will build the core data processing pipeline that serves as the foundation for the entire system.

### Phase 2: Knowledge & Memory (Days 7-12)
Move beyond simple processing to context-aware decision making. Implement Retrieval-Augmented Generation (RAG) to ground AI responses in historical data, manage conversation memory, and build reasoning chains for complex judgments.

### Phase 3: Agents & Tools (Days 13-18)
Transition from passive scripts to active agents. Design and deploy autonomous agents capable of using tools, executing API calls, and collaborating to solve multi-step problems without constant human intervention.

### Phase 4: Autonomous Workflow (Days 19-23)
Orchestrate the complete system into a production-grade workflow. Focus on optimization, consistency checks, and implementing "Human-in-the-Loop" patterns to handle edge cases while automating the majority of the workload.

### Phase 5: Scale & Observability (Days 24-25)
Prepare for production scale. Implement observability, audit trails, and explainability features to trust the system's decisions, culminating in a final high-volume stress test.

---

## 💻 Technical Approach

### Core Principle: Infrastructure as Code

**You must work with actual code and infrastructure.** This challenge cannot be solved by pasting prompts into a web chatbot. You need to:
- Write Python scripts that interact with AWS Bedrock via Boto3
- Define infrastructure using CloudFormation, Terraform, or CDK
- Create Lambda functions and agent configurations
- Build reproducible, shareable solutions

### Cost Management Strategy

AWS services cost real money. To participate responsibly:
1. **Use Infrastructure as Code templates** – Deploy only what you need, when you need it
2. **Destroy resources after each day** – Use `terraform destroy` or equivalent cleanup scripts
3. **Set up budget alerts** – Configure AWS Budgets before starting (see `setup/aws_budget_setup.md`)
4. **Optimize prompts** – Reduce token usage through efficient prompt design
5. **Cache aggressively** – Reuse embeddings, summaries, and model responses where possible

**Estimated daily cost:** $0.50 – $5.00 USD depending on usage patterns.

**Total estimated cost for all 25 days:** $12.50 – $125.00 USD (assuming responsible resource cleanup).

---

## 🛠️ Technical Requirements

### AWS Services Required

| Service | Purpose | Documentation |
|---------|---------|---|
| **Amazon Bedrock** | Foundation models for text, embeddings, and image generation | [Bedrock Docs](https://docs.aws.amazon.com/bedrock/) |
| **Amazon Bedrock Agents** | Multi-agent orchestration and tool use | [Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) |
| **Amazon Bedrock Knowledge Bases** | Vector store for RAG pipelines | [Knowledge Bases Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) |
| **AWS Lambda** | Serverless compute for tool implementations | [Lambda Docs](https://docs.aws.amazon.com/lambda/) |
| **Amazon S3** | Object storage for datasets and outputs | [S3 Docs](https://docs.aws.amazon.com/s3/) |
| **Amazon DynamoDB** | NoSQL database for session state and memory | [DynamoDB Docs](https://docs.aws.amazon.com/dynamodb/) |
| **AWS Step Functions** | Workflow orchestration (optional) | [Step Functions Docs](https://docs.aws.amazon.com/step-functions/) |
| **Amazon CloudWatch** | Logging and monitoring | [CloudWatch Docs](https://docs.aws.amazon.com/cloudwatch/) |

### Software Requirements

- **Python:** 3.9 or higher
- **Package Manager:** pip or uv
- **AWS CLI:** Latest version (for credential management)
- **Git:** For version control and collaboration

### Python Dependencies

Core packages (see `setup/requirements.txt`):
- `boto3` – AWS SDK for Python
- `pandas` – Data manipulation and analysis
- `numpy` – Numerical computing
- `hypothesis` – Property-based testing
- `pytest` – Unit testing framework
- `faker` – Synthetic data generation
- `jinja2` – Template rendering
- `python-dotenv` – Environment variable management

### AWS Account Setup

1. **Create an AWS Account** – Visit [aws.amazon.com](https://aws.amazon.com)
2. **Enable Bedrock** – Request model access in the Bedrock console
3. **Create IAM User** – Set up a dedicated user with programmatic access
4. **Configure Credentials** – Run `aws configure` with your access keys
5. **Set Budget Alerts** – Configure AWS Budgets to monitor spending

See `setup/bedrock_setup_guide.md` and `setup/aws_budget_setup.md` for detailed instructions.

---

## 📂 Repository Structure

```
sleigh-ride-cloud-chronicles/
│
├── README.md (this file)
├── setup/ (installation guides, starter code, budget setup)
├── datasets/ (all shared data: letters, catalogs, behavior logs)
├── resources/ (personas, guidelines, workflow specs)
├── day01/ through day25/ (daily challenges with input/ and output/ folders)
└── utils/ (helper scripts and reusable code modules)
```

Each `dayXX/` folder contains:
- `task.md` – The day's challenge description
- `input/` – Files needed to complete the challenge
- `expected/` – Reference outputs showing what you're aiming for
- `output/` – Where you'll place your generated results

---

## 🎮 Rules & Guidelines

### What You Should Do
1. **Write and share your code** – Create scripts, notebooks, or applications that solve each day's challenge
2. **Use infrastructure-as-code** – Define your AWS resources programmatically so others can reproduce your work
3. **Submit pull requests** – Share your solutions by adding them to your fork and opening a PR
4. **Collaborate and learn** – Discuss approaches, share insights, help others debug
5. **Destroy your infrastructure daily** – Don't leave expensive resources running overnight

### What You Should NOT Do
1. **Do not solve challenges using only online chatbots** – You need actual code and infrastructure
2. **Do not copy/redistribute the story text** – You may link to this repository, but don't republish the narrative chapters
3. **Do not share your AWS credentials** – Use IAM roles, environment variables, and secure practices
4. **Do not create permanent global infrastructure** – Each day should be deployed and destroyed
5. **Do not use this for production workloads** – This is a learning exercise with mock data

---

## 🛠️ Getting Started

### Step 1: Set Up Your AWS Environment

```bash
# Clone this repository
git clone https://github.com/your-org/sleigh-ride-cloud-chronicles.git
cd sleigh-ride-cloud-chronicles

# Run setup script
cd setup
./install.sh

# Configure AWS credentials
aws configure

# Set up budget alerts (IMPORTANT)
# Follow instructions in setup/aws_budget_setup.md
```

### Step 2: Enable Amazon Bedrock

You must enable model access in Amazon Bedrock before starting:
1. Navigate to AWS Console > Amazon Bedrock
2. Go to "Model access" in the left sidebar
3. Request access to Claude 3.5 Sonnet and Titan Embeddings
4. Wait for approval (usually instant for Claude models)

See `setup/bedrock_setup_guide.md` for detailed instructions.

### Step 3: Install Dependencies

```bash
# From the repository root
pip install -r setup/requirements.txt

# Or using uv (faster)
uv pip install -r setup/requirements.txt
```

### Step 4: Start Day 1

```bash
cd day01
cat task.md  # Read the challenge
python solution.py  # Your code goes here
```

### Step 5: Deploy Infrastructure (Example)

```bash
# Using Terraform
cd infrastructure/day07
terraform init
terraform plan
terraform apply

# When done for the day
terraform destroy
```

### Step 6: Share Your Solution

```bash
# Create your solution folder
mkdir -p solutions/your-username/day01
cp your_code.py solutions/your-username/day01/
cp infrastructure.tf solutions/your-username/day01/

# Commit and push
git checkout -b solution-day01-yourname
git add solutions/your-username/day01/
git commit -m "Add Day 1 solution"
git push origin solution-day01-yourname

# Open a pull request on GitHub
```

---

## 💡 Tips for Success
1. **Start simple** – Don't over-engineer early days; complexity builds gradually
2. **Read the story** – Technical hints are woven into the narrative
3. **Use the expected outputs** – They show exactly what format you're targeting
4. **Monitor your AWS costs** – Check billing dashboard daily
5. **Ask for help** – Use GitHub Discussions when you're stuck
6. **Document your decisions** – Future you will thank present you
7. **Test with small datasets first** – Scale up only after your logic works
8. **Destroy infrastructure nightly** – Avoid surprise bills

---

## 🤝 Contributing

We welcome contributions that enhance the learning experience:
- **Bug fixes** in provided datasets or setup scripts
- **Additional utility functions** in the `utils/` directory
- **Documentation improvements** for setup or technical concepts
- **Infrastructure templates** for common patterns
- **Your completed solutions** via pull request

Please open an issue before making major changes to the core challenge structure.

---

## ⚠️ Important Disclaimers

### Cost Responsibility
You are responsible for all AWS charges incurred while participating in this challenge. Set up budget alerts and destroy resources daily. This project is provided as-is with no warranty regarding costs.

### Educational Purpose
This challenge uses mock data and simplified scenarios. Real-world production systems require additional security, compliance, monitoring, and architectural considerations not covered here.

### Not Affiliated with Amazon
This is an independent educational project. It is not created by, affiliated with, or endorsed by Amazon Web Services, Inc.

---

## 📄 License & Attribution

**Sleigh-Ride Cloud Chronicles** © 2024. All story content, narrative text, character descriptions, and challenge designs are proprietary.

You may:
- Link to this repository
- Reference the challenges in discussions, blog posts, or educational contexts
- Share your own solution code and infrastructure templates
- Use this challenge for personal learning or team training

You may **not**:
- Republish the story text or challenge descriptions on other platforms
- Create derivative works that replicate the narrative or challenge structure
- Use the name "Sleigh-Ride Cloud Chronicles" for other projects
- Redistribute the complete dataset or narrative content

Your solution code and infrastructure definitions are your own and may be licensed as you choose.

---

## 🎄 Ready to Begin?

Santa is waiting at the North Pole, and Christmas hangs in the balance.

Read `day01/task.md` to begin your journey.

The Cloud Migration starts now.

---

**Happy Building, and May Your Pipelines Never Fail!**

*- The Sleigh-Ride Cloud Chronicles Team*
