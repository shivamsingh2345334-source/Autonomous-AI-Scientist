import os
import chromadb
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


db_client = chromadb.Client()
collection = db_client.get_or_create_collection(name="research_memory")


llm = ChatGroq(
    temperature=0.6,
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

def autonomous_research_cycle(topic, background):
    print(f"\n🧐 RESEARCH INITIATED: {topic}")
    print("-" * 30)

    # --- PHASE 1: THE PLANNER (Generation) ---
    planner_prompt = f"Topic: {topic}\nContext: {background}\nTask: Propose a unique research hypothesis and a 3-step experiment plan."
    plan = llm.invoke([
        SystemMessage(content="You are a Visionary Scientist."),
        HumanMessage(content=planner_prompt)
    ]).content
    print("🚀 PHASE 1: Plan Generated.")

    # --- PHASE 2: THE CRITIC (Evaluation) ---
    critic_prompt = f"Review this Research Plan:\n{plan}\n\nTask: Identify 3 critical flaws, technical risks, or gaps."
    critique = llm.invoke([
        SystemMessage(content="You are a Skeptical Senior Reviewer."),
        HumanMessage(content=critic_prompt)
    ]).content
    print("🧐 PHASE 2: Critique Received.")

    # --- PHASE 3: FINAL REFINEMENT (Synthesis) ---
    refine_prompt = f"Original Plan: {plan}\nCritic's Feedback: {critique}\n\nTask: Rewrite the plan by addressing all concerns."
    final_output = llm.invoke([
        SystemMessage(content="You are a Lead Lab Director."),
        HumanMessage(content=refine_prompt)
    ]).content
    print("🏆 PHASE 3: Final Scientific Plan Synthesized.")

    # 3. Persistent Memory Injection
    collection.add(
        documents=[final_output],
        metadatas=[{"topic": topic, "status": "refined"}],
        ids=[f"research_{topic.replace(' ', '_').lower()}"]
    )
    
    return plan, critique, final_output

if __name__ == "__main__":
    user_topic = "Developing a Carbon-Capture material using Graphene"
    user_bg = "Current materials are too expensive for large scale industrial use."

    initial, review, final = autonomous_research_cycle(user_topic, user_bg)

    print("\n" + "="*50)
    print(f"🔬 FINAL REFINED PLAN:\n\n{final}")
    print("="*50)
EOF
