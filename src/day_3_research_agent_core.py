"""
Autonomous Experiment Engine
Single-file implementation for simplicity and clarity.

Responsibilities:
- LLM-driven autonomous code generation
- Safe execution with stdout/error capture
- Self-healing retry loop
- Centralized configuration usage
"""

# =====================================================
# IMPORTS
# =====================================================

import sys
from io import StringIO
from langchain_core.messages import SystemMessage, HumanMessage

# =====================================================
# CONFIG (imported from config/settings.py)
# =====================================================

from config.settings import (
    MAX_RETRIES,
    SYSTEM_ROLE,
)

# =====================================================
# EXECUTION ENGINE
# =====================================================

def run_code_logic(code_string: str) -> dict:
    """
    Executes dynamically generated Python code
    and safely captures stdout or runtime errors.
    """
    old_stdout = sys.stdout
    buffer = sys.stdout = StringIO()

    try:
        exec(code_string, {})
        sys.stdout = old_stdout
        return {
            "status": "success",
            "output": buffer.getvalue()
        }

    except Exception as e:
        sys.stdout = old_stdout
        return {
            "status": "error",
            "output": str(e)
        }

# =====================================================
# AUTONOMOUS LLM AGENT
# =====================================================

def generate_code(llm, task: str, feedback: str) -> str:
    """
    Uses LLM to generate executable Python code
    based on task description and previous errors.
    """

    prompt = f"""
Task: {task}

Previous Error (if any):
{feedback}

Instructions:
- Use synthetic data only
- Print the final result clearly
- Respond ONLY with executable Python code
"""

    response = llm.invoke([
        SystemMessage(content=SYSTEM_ROLE),
        HumanMessage(content=prompt)
    ]).content

    return (
        response
        .replace("```python", "")
        .replace("```", "")
        .strip()
    )

# =====================================================
# AUTONOMOUS EXPERIMENT RUNNER
# =====================================================

def autonomous_experiment_runner(llm, task: str) -> str:
    """
    Orchestrates the full autonomous experiment lifecycle:
    code generation → execution → feedback → retry.
    """

    print(f"🔬 Mission Started: {task}")
    feedback = ""

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n🚀 Attempt {attempt}")

        code = generate_code(llm, task, feedback)
        result = run_code_logic(code)

        if result["status"] == "success":
            print("✅ Experiment Successful")
            return result["output"]

        print(f"❌ Error Encountered:\n{result['output']}")
        feedback = result["output"]

    return "❌ Experiment failed after maximum retries."

# =====================================================
# OPTIONAL ENTRY POINT (for local testing)
# =====================================================

if __name__ == "__main__":
    print("🔥 Autonomous Experiment Engine Ready")
