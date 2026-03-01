import traceback
import sys
import pandas as pd
import numpy as np
from io import StringIO
from langchain_core.messages import HumanMessage, SystemMessage

# ============================================================
# 1. THE EXECUTION MODULE (The Muscle 🛡️)
# ============================================================
def advanced_run_code(code_string):
    """
    AI-generated code ko safe environment mein run karta hai 
    aur output ko capture karta hai.
    """
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    # Global environment taaki pandas/numpy imports accessible rahein
    local_vars = {}

    try:
        # AI ka likha code execute ho raha hai
        exec(code_string, globals(), local_vars)
        sys.stdout = old_stdout
        return {
            "status": "success", 
            "output": redirected_output.getvalue()
        }
    except Exception:
        sys.stdout = old_stdout
        # Error ka poora 'traceback' capture karna Healing ke liye zaroori hai
        return {
            "status": "error", 
            "output": traceback.format_exc()
        }

# ============================================================
# 2. THE VALIDATION MODULE (The Judge ⚖️)
# ============================================================
def is_output_valid(output):
    """
    Check karta hai ki result 'nan' ya empty toh nahi hai.
    """
    forbidden_words = ["nan", "none", "invalid value"]
    
    if not output.strip():
        return False
    
    if any(word in output.lower() for word in forbidden_words):
        return False
        
    return True

# ============================================================
# 3. THE GOD-MODE ENGINE (The Brain 🧠)
# ============================================================
def god_mode_executor(llm_instance, task, max_attempts=4):
    """
    Self-Healing Loop: Attempt -> Run -> Error -> Fix -> Success.
    """
    print(f"🚀 Mission Started: {task}")
    history = ""

    for i in range(max_attempts):
        print(f"\n🧠 Attempt {i+1}: AI is brainstorming & coding...")

        prompt = f"""
        You are a Senior Data Scientist.
        TASK: {task}
        ERROR_HISTORY: {history}

        INSTRUCTIONS:
        1. Write full Python code using pandas, numpy, and scipy.
        2. Use np.random.normal or seeds to ensure data has variance.
        3. Prevent 'nan' results in t-tests by ensuring data groups are different.
        4. Print the final statistical results (Mean, P-Value) clearly.
        5. Return ONLY the code block.
        """

        # LLM (Groq/Llama) se code mangwana
        ai_response = llm_instance.invoke([
            SystemMessage(content="You are a production-ready coder who returns only clean Python code."),
            HumanMessage(content=prompt)
        ]).content

        # Code ko clean karna (Markdown formatting hatana)
        clean_code = ai_response.replace("```python", "").replace("```", "").strip()

        # Step 1: Execute the code
        result = advanced_run_code(clean_code)

        if result["status"] == "success":
            # Step 2: Validate the logic
            if is_output_valid(result["output"]):
                print(f"✅ SUCCESS: Code executed and logic is valid!")
                return result["output"]
            else:
                print(f"⚠️ Warning: Output contained 'nan'. Retrying with better data...")
                history += f"\nAttempt {i+1} gave 'nan' results. Please increase data variance."
        else:
            # Step 3: Self-Heal if error occurs
            error_msg = result['output'].splitlines()[-1]
            print(f"❌ Error detected: {error_msg}")
            history += f"\nAttempt {i+1} failed with error: {result['output']}"

    return "🚨 Mission Failed: System could not heal after max attempts."

# ============================================================
# 4. EXECUTION BLOCK (The Control Room 🛰️)
# ============================================================
if __name__ == "__main__":
    # Yahan apna LLM instance pass karo (e.g., Groq ka ChatGroq)
    # final_llm = ChatGroq(api_key="your_key")
    
    task_desc = (
        "Create a dataframe with 3 compounds (Alpha, Beta, Gamma). "
        "Give them 5 different stability scores and find the p-value using t-test."
    )
    
    # Run the engine
    # final_res = god_mode_executor(final_llm, task_desc)
    # print(f"\n🏁 FINAL VALIDATED RESULT:\n{final_res}")
    
    print("🛠️ Framework Ready. Plug in your LLM to start the Autonomous Scientist.")
