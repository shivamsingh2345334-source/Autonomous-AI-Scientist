import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import chromadb

# ============================
# DAY 2: Autonomous Research Scientist
# ============================

# Memory Engine (Persistent Research Memory)
db_client = chromadb.Client()
collection = db_client.get_or_create_collection(
    name="autonomous_research_memory"
)

# LLM Brain (Groq + LLaMA 3.3)
llm = ChatGroq(
    temperature=0.6,
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

def autonomous_research_cycle(topic: str, background: str):
    print(f"🧪 Research Session Started: {topic}\n")

    # PHASE 1: PLANNER
    planner_prompt = f"""
    You are an AI Research Scientist.

    Topic: {topic}
    Background Context: {background}

    Task:
    1. Propose ONE novel research hypothesis.
    2. Design a 3-step technical experimental plan.
    """

    plan = llm.invoke([
        SystemMessage(content="You are a visionary scientific researcher."),
        HumanMessage(content=planner_prompt)
    ]).content

    print("🚀 Planner generated initial hypothesis.\n")

    # PHASE 2: CRITIC
    critic_prompt = f"""
    Review the following research plan critically:

    {plan}

    Identify:
    - Technical flaws
    - Logical gaps
    - Feasibility risks
    Provide at least 3 points.
    """

    critique = llm.invoke([
        SystemMessage(content="You are a skeptical senior peer reviewer."),
        HumanMessage(content=critic_prompt)
    ]).content

    print("🧐 Critic analysis complete.\n")

    # PHASE 3: REFINEMENT
    refine_prompt = f"""
    Original Plan:
    {plan}

    Critic Feedback:
    {critique}

    Task:
    Rewrite the research plan by fixing ALL issues.
    Make it executable, realistic, and scientifically rigorous.
    """

    final_plan = llm.invoke([
        SystemMessage(content="You are a principal investigator."),
        HumanMessage(content=refine_prompt)
    ]).content

    # Save to Memory
    collection.add(
        documents=[final_plan],
        metadatas=[{"topic": topic}],
        ids=[f"day2_{topic.replace(' ', '_')}"]
    )

    return plan, critique, final_plan


# ----------------------------
# TEST RUN
# ----------------------------
if __name__ == "__main__":
    topic = "Developing a Carbon-Capture material using Graphene"
    background = "Current carbon capture materials are expensive and inefficient at scale."

    initial, review, final = autonomous_research_cycle(topic, background)

    print("\n" + "="*60)
    print("🏆 FINAL REFINED SCIENTIFIC PLAN\n")
    print(final)
    print("="*60)
