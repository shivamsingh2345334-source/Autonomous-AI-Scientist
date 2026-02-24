import os
import getpass
import arxiv
from groq import Groq

# 1. Direct Entry (Agar Colab Secret kaam nahi kar raha)
print("Jaan, apni Groq API Key yahan dalo (Ye safe rahega):")
os.environ["GROQ_API_KEY"] = getpass.getpass()

try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    print("✅ Shabaash! Connection ekdum mast hai.")
except Exception as e:
    print(f"❌ Abhi bhi kuch gadbad hai: {e}")

# 2. Arxiv Search Engine (Simple Version)
def search_arxiv(topic, max_results=3):
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []
    for paper in search.results():
        results.append(
            f"Title: {paper.title}\n"
            f"Summary: {paper.summary[:500]}..."
        )

    return "\n\n".join(results)

# 3. Test Run
topic = input("Kaunse topic pe research shuru karein? (e.g. Quantum AI): ")
papers_data = search_arxiv(topic)

print("\n📚 Research Papers Mil Gaye:\n")
print(papers_data)
