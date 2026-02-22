import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer


class ResearchMemory:
    """
    Persistent Memory System for an AI Scientist.
    Stores past research tasks, code, and results
    so the AI does not repeat previous mistakes.
    """

    def __init__(self):
        # Persistent ChromaDB client
        self.client = chromadb.PersistentClient(path="./research_vault")
        self.collection = self.client.get_or_create_collection(
            name="ai_scientist_memory"
        )

        # Sentence embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("🧠 Memory Vault Online: AI ab purani galtiyan nahi dohrayega!")

    def store_experience(self, task, code, result):
        """
        Store a research experience in vector memory.
        """
        embedding = self.model.encode(task).tolist()

        self.collection.add(
            embeddings=[embedding],
            documents=[f"Task: {task}\nCode: {code}\nResult: {result}"],
            ids=[f"exp_{np.random.randint(1000, 9999)}"]
        )

        print(f"💾 Saved: {task[:30]}... has been committed to memory.")

    def retrieve_relevant_memory(self, current_task):
        """
        Retrieve the most relevant past experience
        for a given new task.
        """
        query_embedding = self.model.encode(current_task).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=1
        )

        if results and results["documents"] and len(results["documents"][0]) > 0:
            return results["documents"][0][0]

        return "No past experience found."


# ----------------- TEST RUN -----------------
if __name__ == "__main__":
    memory_vault = ResearchMemory()

    print("\n--- Testing Phase ---")
    memory_vault.store_experience(
        "T-test on Graphene",
        "import scipy; stats.ttest_ind(...)",
        "p-value: 0.04"
    )

    context = memory_vault.retrieve_relevant_memory(
        "Perform stability analysis on Carbon nanotubes"
    )

    print(f"\n🧠 AI's Recalled Memory:\n{context}")
