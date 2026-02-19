"""
Day 5 Module: Web-Integrated AI Research Synthesizer

Ye module:
- Tavily se web data fetch karta hai
- Groq LLM se scientific abstract generate karta hai
- Clean architecture follow karta hai
- API keys environment variables se leta hai
"""

import os
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv
from typing import Optional


# -------------------------------------------------------
# Environment Setup
# -------------------------------------------------------

load_dotenv()  # .env file load karega

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in environment variables.")

if not TAVILY_API_KEY:
    raise ValueError("❌ TAVILY_API_KEY not found in environment variables.")


# -------------------------------------------------------
# Core Scientist Class
# -------------------------------------------------------

class GroqScientist:
    """
    Ye class:
    - Web se data collect karegi
    - LLM ko context degi
    - Professional scientific abstract generate karegi
    """

    def __init__(self, topic: str, temperature: float = 0.4):
        self.topic = topic
        self.temperature = temperature

        self.groq_client = Groq(api_key=GROQ_API_KEY)
        self.tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

    # -----------------------------
    # Web Data Retrieval
    # -----------------------------
    def fetch_web_data(self) -> Optional[str]:
        """
        Tavily API se web search karega.
        Safe handling ke saath.
        """
        try:
            response = self.tavily_client.search(query=self.topic)

            if response and "results" in response and len(response["results"]) > 0:
                return response["results"][0]["content"]
            else:
                return "No relevant web data found."

        except Exception as e:
            return f"Web search failed: {str(e)}"

    # -----------------------------
    # LLM Interaction
    # -----------------------------
    def generate_abstract(self, web_context: str) -> str:
        """
        Groq LLM ko scientific abstract generate karne ke liye call karega.
        """
        prompt = f"""
        You are a Senior AI Scientist.

        Based on the following web research data:
        {web_context}

        Write a 3-paragraph professional scientific abstract about:
        {self.topic}

        Tone:
        - Highly technical
        - Research-grade
        - Formal academic language
        """

        completion = self.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )

        return completion.choices[0].message.content

    # -----------------------------
    # Main Pipeline
    # -----------------------------
    def synthesize_research(self) -> str:
        """
        Full Day 5 pipeline:
        Web → LLM → Scientific Report
        """
        print(f"🚀 Initiating research synthesis on: {self.topic}")

        web_data = self.fetch_web_data()
        final_report = self.generate_abstract(web_data)

        return final_report


# -------------------------------------------------------
# Example Execution
# -------------------------------------------------------

if __name__ == "__main__":
    topic = "Quantum Computing in Drug Discovery"

    scientist = GroqScientist(topic=topic)
    report = scientist.synthesize_research()

    print("\n🔬 GENERATED SCIENTIFIC ABSTRACT:\n")
    print(report)
