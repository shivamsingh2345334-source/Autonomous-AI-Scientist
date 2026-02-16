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
    print(f"🧐 Starting Research on: {topic}...")
    plan = llm.invoke([SystemMessage(content="You are a Visionary Scientist."),
                       HumanMessage(content=f"Topic: {topic}\nContext: {background}")]).content
    critique = llm.invoke([SystemMessage(content="You are a Skeptical Senior Reviewer."),
                           HumanMessage(content=f"Review: {plan}")]).content
    final = llm.invoke([SystemMessage(content="You are a Lead Lab Director."),
                               HumanMessage(content=f"Original: {plan}\nCritique: {critique}")]).content
    return final

if __name__ == "__main__":
    print(autonomous_research_cycle("Carbon Capture", "Industrial Graphene"))
