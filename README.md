# Autonomous AI Scientist 🧠🤖

Day-1 Prototype of an AI Scientist that:
- Accepts a research topic
- Searches Arxiv papers automatically
- Prepares structured research inputs

## Day-1 Features
- Secure Groq API connection
- Live Arxiv paper retrieval
- Clean & minimal research pipeline

## How to Run
```bash
pip install -r requirements.txt
python src/day1_entry.py
Vision

This project will evolve into a fully autonomous research scientist capable of:

Reading papers

Forming hypotheses

Designing experiments

Publishing insights


----------------------------------------------



🔬 Autonomous AI Scientist
Day-2: Self-Critiquing Research Intelligence
🚀 What Changed in Day-2?

Day-2 introduces a true Autonomous Research Agent that can:

Generate a novel research hypothesis

Critically review its own idea (like a senior scientist)

Refine the plan into an execution-ready research proposal

Persist research memory using a vector database

This transforms the system from a paper fetcher (Day-1) into a thinking scientific entity.

🧠 Core Capability Added (Day-2)
Capability	Description
🧪 Planner	Proposes original hypotheses + experiments
🧐 Critic	Identifies logical, technical, and scientific flaws
🛠 Refiner	Produces a corrected, execution-ready plan
🧠 Memory	Stores refined research using ChromaDB

⚠️ This is not prompt chaining.
This is a closed-loop reasoning system with memory.

🏗️ Architecture Overview (Day-2)
User Topic
   │
   ▼
[ Planner Agent ]
   │
   ▼
[ Critic Agent ]
   │
   ▼
[ Refinement Agent ]
   │
   ▼
[ Vector Memory (ChromaDB) ]

Each stage is role-conditioned, ensuring diverse scientific perspectives:

Visionary Scientist

Skeptical Reviewer

Lead Lab Director



---------------------------------
#day 3
# 🧠 Autonomous Experiment Engine

A production-ready framework for autonomous AI experiments.

## Features
- LLM-driven code generation
- Safe execution
- Self-healing retry loop
- Modular architecture

## Use Cases
- AI research
- Data science automation
- Autonomous agents



# 🧪 AI Drug Efficacy Statistical Analyst  
### Day 4 — Research-Grade Statistical Intelligence Engine

> **An AI-powered statistical validation system for experimental drug efficacy, designed for modern AI-driven R&D pipelines.**

---

## 🚀 Why This Project Exists

In real-world **drug discovery and biotech R&D**, teams test **dozens or hundreds of compounds**.  
The biggest mistake early-stage research makes?

❌ Choosing compounds based on **intuition**  
❌ Relying on **raw averages**  
❌ Ignoring **statistical significance**

This project solves that.

---

## 🎯 Core Problem

Given experimental drug efficacy data:

- How do we **objectively validate** results?
- How do we **filter noise vs signal**?
- How do we **decide which compound deserves deeper research investment**?

Manual analysis is:
- Slow
- Error-prone
- Not scalable

---

## ✅ Solution Overview

This repository introduces a **Statistical Analyst AI Agent** that:

✔ Performs **hypothesis testing** using classical statistics  
✔ Evaluates results against a **baseline efficacy threshold**  
✔ Automatically identifies **top-performing compounds**  
✔ Generates **interactive dashboards** for human + AI decision-makers  

This is **how real research labs work**.

---

## 🧠 Intelligence Layer (What Makes It Special)

### 1️⃣ Statistical Validation (Not Guesswork)
- One-sample **t-test**
- Null hypothesis: *compound efficacy ≤ baseline*
- Confidence-driven decision logic

### 2️⃣ Autonomous Decision Engine
- P-value driven branching
- Automatically recommends **next research focus**
- Eliminates emotional bias

### 3️⃣ Visual Intelligence
- Interactive Plotly dashboards
- Color-scaled efficacy mapping
- Executive-level interpretability

---

## 🏗️ System Architecture


Raw Experimental Data
↓
DataFrame Normalization
↓
Statistical Analysis Engine
↓
Hypothesis Testing (t-test)
↓
Compound Ranking
↓
Interactive Visualization
↓
AI Research Decision Output



## 🧪 Example Usage

```python
from src.analyst import AI_Analyst

data = {
    "compound": ["Alpha-7", "Beta-2", "Gamma-9"],
    "efficacy": [42, 88, 35],
    "molecular_weight": [250.4, 310.2, 280.5]
}

analyst = AI_Analyst()
decision, dashboard = analyst.perform_analysis(data)

print(decision)
dashboard.show()




# 🚀 Groq Scientist

An autonomous AI research assistant that performs real-time web retrieval and synthesizes professional scientific abstracts using Groq LLM.

## 🔬 Features
- Lightning-fast inference via Groq
- Retrieval-Augmented Generation (RAG)
- Fully autonomous scientific summarization

## ⚙️ Tech Stack
- Groq LLM (Llama 3.3 70B)
- Tavily Search API
- Python

🎯 Use Cases

Rapid literature reviews

Startup R&D analysis

Scientific hypothesis exploration



## 🔬 Example Output

> Topic: Quantum Computing in Drug Discovery

The nascent realm of quantum computing has precipitated a paradigmatic shift in computational science...
