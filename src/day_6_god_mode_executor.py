"""
god_mode_executor.py

Self-healing execution loop that asks an LLM to generate Python code,
runs it safely, validates output, and retries if needed.

Before running:
- Configure your LLM (LangChain / OpenAI / etc.)
- Replace the `llm` placeholder with your actual model.
"""

import traceback
import sys
from io import StringIO
import pandas as pd

# Optional: Uncomment and configure if using LangChain
# from langchain.schema import SystemMessage, HumanMessage

# =========================
# LLM PLACEHOLDER
# =========================
class DummyLLM:
    """
    Replace this with your real LLM client.
    """
    def invoke(self, messages):
        raise NotImplementedError(
            "Configure your LLM before running. Replace DummyLLM."
        )

llm = DummyLLM()


# =========================
# Execution Engine
# =========================
def advanced_run_code(code_string):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    local_vars = {}

    try:
        exec(code_string, globals(), local_vars)
        sys.stdout = old_stdout
        return {"status": "success", "output": redirected_output.getvalue()}
    except Exception:
        sys.stdout = old_stdout
        return {"status": "error", "output": traceback.format_exc()}


# =========================
# Output Validator
# =========================
def is_output_valid(output):
    forbidden_words = ["nan", "none", "invalid value"]
    if not output.strip() or any(word in output.lower() for word in forbidden_words):
        return False
    return True


# =========================
# Self-Healing Loop
# =========================
def god_mode_executor(task, max_attempts=4):
    print(f"🚀 Mission Started: {task}")
    history = ""

    for i in range(max_attempts):
        print(f"\n🧠 Attempt {i+1}: AI is brainstorming...")

        prompt = f"""
You are a Senior Data Scientist.
TASK: {task}
ERROR_HISTORY: {history}

INSTRUCTIONS:
1. Write full Python code.
2. Ensure data variance so t-tests do not return NaN.
3. Print results clearly.
4. Return ONLY code.
"""

        try:
            ai_response = llm.invoke([
                # SystemMessage(content="You are a production-ready coder."),
                # HumanMessage(content=prompt)
                prompt  # Simple fallback if not using LangChain message objects
            ])
            content = getattr(ai_response, "content", str(ai_response))
        except Exception as e:
            return f"LLM not configured: {e}"

        clean_code = content.replace("```python", "").replace("```", "").strip()

        result = advanced_run_code(clean_code)

        if result["status"] == "success":
            if is_output_valid(result["output"]):
                print("✅ SUCCESS: Valid output obtained.")
                return result["output"]
            else:
                print("⚠️ Invalid output detected. Retrying...")
                history += f"\nAttempt {i+1} invalid output: {result['output']}"
        else:
            print("❌ Execution error encountered.")
            history += f"\nAttempt {i+1} error: {result['output']}"

    return "Mission Failed: Maximum attempts reached."


# =========================
# Main Entry
# =========================
if __name__ == "__main__":
    task_desc = (
        "Create a dataframe with 3 compounds (Alpha, Beta, Gamma). "
        "Assign 5 different stability scores and compute t-test p-value."
    )

    final_res = god_mode_executor(task_desc)

    print("\n🏁 FINAL RESULT:")
    print(final_res)
````
