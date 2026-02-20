# 🚀 Day 3 – Autonomous Experiment Execution Engine

## 🧠 Problem Statement

Modern AI systems can generate code.

But a major limitation exists:

- AI writes code.
- Human manually runs it.
- If error occurs → Human fixes prompt.
- Retry cycle is manual.
- No self-correction loop.

This creates a bottleneck in autonomous experimentation.

We needed a system that:

✔ Generates Python code  
✔ Executes it automatically  
✔ Detects runtime errors  
✔ Feeds errors back to the AI  
✔ Retries intelligently  
✔ Stops only after success  

In short:

We needed an **Autonomous Self-Correcting Code Execution Engine**.

---

## 🎯 Objective

Build a system that can:

1. Accept a research task.
2. Ask the LLM to write Python code.
3. Execute that code dynamically.
4. Capture output or error.
5. Retry with feedback.
6. Return successful result automatically.

No human intervention.

---

## 🏗 Architecture Overview

### 🔹 1. Code Execution Layer

- Uses `exec()` to run dynamic Python code.
- Redirects stdout using `StringIO`.
- Captures both output and errors.
- Returns structured response.

### 🔹 2. Autonomous Retry Loop

- Sends task to LLM.
- Runs returned code.
- If error → sends error back to LLM.
- Retries up to defined limit.
- Stops when success is achieved.

### 🔹 3. Synthetic Data Strategy

As selected earlier:
- No real-world API dependency.
- Uses synthetic data generation.
- Ensures reproducibility.
- Safe experimental environment.

---
