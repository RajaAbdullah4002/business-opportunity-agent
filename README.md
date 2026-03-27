# 🎯 Business Opportunity Intelligence Agent

An AI-powered multi-agent system that automatically researches, scores, and summarises 
business opportunities for any company profile. Built with LangGraph, Claude AI, and Streamlit.

## 🏗️ Architecture

The agent uses a LangGraph state machine with 3 specialised nodes:
```
START → Researcher → Scorer → Summariser → END
```

- **Researcher** — finds 3 realistic business opportunities based on the company profile
- **Scorer** — rates each opportunity 1-10 on relevance, win probability, and revenue impact
- **Summariser** — writes an executive brief with a clear recommended next action

## 🛠️ Tech Stack

- **LangGraph** — graph-based agent orchestration and state management
- **Anthropic Claude API** — LLM powering all 3 agents
- **Streamlit** — rapid web UI prototyping
- **Python 3.11** — core language
- **python-dotenv** — secure API key management

## 🚀 How to Run Locally

1. Clone the repo
```
git clone https://github.com/RajaAbdullah4002/business-opportunity-agent.git
cd business-opportunity-agent
```

2. Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Add your API key — create a `.env` file:
```
ANTHROPIC_API_KEY=your-key-here
```

5. Run the app
```
streamlit run main.py
```

## 💡 Key Concepts Demonstrated

- **Agentic AI architecture** — multiple specialised agents with distinct roles
- **LangGraph state machines** — structured, observable agent flow
- **Prompt engineering** — formatting outputs for consistent, parseable results
- **State management** — shared AgentState TypedDict passed between all nodes
- **Secure secret handling** — API keys via .env, never hardcoded

## 📸 Screenshot
<img width="1273" height="611" alt="OPPO" src="https://github.com/user-attachments/assets/d4e8614c-576a-4315-961f-d56e245bb1cf" />




## 👤 Author

**Roger (Raja Abdullah)**  
Melbourne, VIC, Australia  
[LinkedIn](https://www.linkedin.com/in/mabdullah010) | [GitHub](https://github.com/RajaAbdullah4002)
