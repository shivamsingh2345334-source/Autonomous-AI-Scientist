import os
import getpass
import arxiv
from groq import Groq

# 1. API Connection Logic
print("Jaan, apni Groq API Key yahan dalo (Ye safe rahega):")
api_key = getpass.getpass() 
os.environ["GROQ_API_KEY"] = api_key

try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    print("✅ Shabaash! Connection ekdum mast hai.")
except Exception as e:
    print(f"❌ Abhi bhi kuch gadbad hai: {e}")

# 2. Arxiv Search Engine
def search_arxiv(topic, max_results=3):
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    results = []
    for paper in search.results():
        results.append(f"Title: {paper.title}\nSummary: {paper.summary[:500]}...")
    return "\n\n".join(results)

# 3. Test Run
if __name__ == "__main__":
    topic = input("Kaunse topic pe research shuru karein? (e.g. Quantum AI): ")
    papers_data = search_arxiv(topic)
    print(f"\n📚 Research Papers Mil Gaye:\n{papers_data[:500]}...")
