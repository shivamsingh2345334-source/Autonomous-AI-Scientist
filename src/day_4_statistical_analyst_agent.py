"""
Module: Statistical Analyst Agent
Project: Nexus-Core / AI Scientist Assistant
Role: Performs automated statistical validation (T-Test) and 
      generates interactive decision-making dashboards.
"""

import pandas as pd
import plotly.express as px
import numpy as np
from scipy import stats

class AI_Analyst:
    """
    Autonomous Statistical Agent that validates experimental data 
    and determines research significance.
    """
    
    def __init__(self):
        print("📊 Nexus-Core: Statistical Analyst Agent is Online.")

    def perform_analysis(self, raw_data):
        """
        Input: Dictionary/JSON containing experimental results.
        Process: Normalization -> T-Test Calculation -> Dashboard Generation.
        Output: (String Insight, Plotly Figure)
        """
        # 1. Data Processing
        df = pd.DataFrame(raw_data)

        # 2. Statistical Computations (Inferential Stats)
        # Testing if efficacy mean is significantly different from a baseline (50)
        t_stat, p_val = stats.ttest_1samp(df['efficacy'], 50)

        # 3. Interactive Visualization with Plotly
        fig = px.bar(
            df, 
            x='compound', 
            y='efficacy',
            title="🧪 Drug Efficacy: Statistical Validation Pipeline",
            labels={'efficacy': 'Efficacy Score (%)', 'compound': 'Chemical Compound'},
            color='efficacy',
            text='efficacy',
            color_continuous_scale='Viridis',
            hover_data=['molecular_weight']
        )

        fig.update_traces(texttemplate='%{text}', textposition='outside')
        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Compound ID",
            yaxis_title="Efficacy (%)",
            font=dict(family="Courier New, monospace", size=12, color="white")
        )

        # 4. Autonomous Decision Logic
        best_idx = df['efficacy'].idxmax()
        top_compound = df.iloc[best_idx]['compound']

        decision = f"Analysis Result: P-Value is {p_val:.4f}. "
        if p_val < 0.05:
            decision += f"The results are statistically significant! 🚀 Proceeding to Deep-Dive on {top_compound}."
        else:
            decision += "Results are within noise levels (p > 0.05). Need to pivot research strategy for Day 5."

        return decision, fig

# --- Deployment Example ---
if __name__ == "__main__":
    experimental_results = {
        'compound': ['Alpha-7', 'Beta-2', 'Gamma-9', 'Delta-4', 'Epsilon-1'],
        'efficacy': [42, 88, 35, 71, 55],
        'molecular_weight': [250.4, 310.2, 280.5, 410.1, 190.9]
    }

    analyst = AI_Analyst()
    insight, dashboard = analyst.perform_analysis(experimental_results)

    print(f"\n💡 AI DECISION ENGINE: \n{insight}")
    # dashboard.show() # Uncomment to render in browser
