import os
from groq import Groq
from tavily import TavilyClient


class GroqScientist:
    """
    Autonomous AI Scientist that performs:
    1. Web retrieval using Tavily
    2. Scientific synthesis using Groq LLM
    """

    def __init__(self, topic, groq_api_key, tavily_api_key):
        self.topic = topic
        self.client = Groq(api_key=groq_api_key)
        self.tavily = TavilyClient(api_key=tavily_api_key)

    def fetch_web_data(self):
        """Fetch top web content related to the research topic."""
        results = self.tavily.search(query=self.topic)
        return results["results"][0]["content"]

    def ask_groq(self, prompt):
        """Send prompt to Groq LLM."""
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content

    def synthesize_research(self):
        """Generate a professional scientific abstract."""
        print(f"🚀 Groq analyzing: {self.topic}")

        web_data = self.fetch_web_data()

        prompt = f"""
        You are a Senior AI Scientist.
        Based on this web data: {web_data},
        write a 3-paragraph professional scientific abstract about {self.topic}.
        Make it highly technical and sophisticated.
        """

        return self.ask_groq(prompt)


if __name__ == "__main__":
    scientist = GroqScientist(
        topic="Quantum Computing in Drug Discovery",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
    )

    report = scientist.synthesize_research()
    print("\n🔬 FINAL SCIENTIFIC ABSTRACT:\n")
    print(report)
