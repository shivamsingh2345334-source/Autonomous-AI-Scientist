# 📓 Day 1: Environment Setup & Paper Acquisition 🧬

## 🚩 The Problem (Challenge)
"Initial setup ke waqt sabse bada challenge tha **Environment Security** aur **Data Ingestion**. Google Colab par API keys ko expose karna unsafe hota hai (security risk), aur Arxiv API se relevant research data ko filter karke fetch karna thoda tricky tha kyunki raw response bahut messy hota hai jise direct LLM ko nahi diya ja sakta."

## 💡 The Solution (Engineering Logic)
Maine is problem ko solve karne ke liye 3-step architecture follow kiya:

1. **Security First:** `getpass` library ka use karke API keys ko runtime memory mein load kiya. Isse sensitive keys GitHub commits ya logs mein leak nahi hongi.
2. **Modular Ingestion:** `arxiv` library ke upar ek wrapper function likha jo search results ko clean string format mein convert karta hai. Maine results ko limit kiya taaki context window overflow na ho.
3. **High-Speed Inference:** **Groq SDK** ko initialize kiya LLaMA-3.1 model ke liye, taaki humein real-time response mile (Sub-second latency).

## 🛠️ Implementation Details
- **Tooling:** Python, Groq Cloud API, Arxiv API.
- **Security:** In-memory environment variables.
- **Logic:** Top-K relevance sorting for research papers.

## ✅ Outcome
Ab system kisi bhi scientific topic par latest research summaries fetch kar sakta hai aur **Groq Inference Engine** ke saath securely communicate karne ke liye taiyar hai. Ye hamare "Autonomous Scientist" ka dimaag (LLM) aur aankhein (Data Source) set-up karne ka pehla kadam hai.
