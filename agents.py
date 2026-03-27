from anthropic import Anthropic
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from dotenv import load_dotenv
import os

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class AgentState(TypedDict):
    company_profile: str
    opportunities: List[str]
    scores: List[str]
    summary: str
    
def researcher(state: AgentState) -> AgentState:
    print("🔍 Researcher is working...")
    
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a business opportunity researcher.
                Based on this company profile: {state['company_profile']}
                
                Find and list 3 realistic business opportunities for them.
                Format each opportunity on a new line starting with a number.
                Be specific and realistic."""
            }
        ]
    )
    
    opportunities = response.content[0].text
    return {**state, "opportunities": [opportunities]}

def scorer(state: AgentState) -> AgentState:
    print("📊 Scorer is working...")
    
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a business opportunity scorer.
                
                Company profile: {state['company_profile']}
                
                Opportunities found:
                {state['opportunities'][0]}
                
                Score each opportunity from 1-10 based on:
                - Relevance to the company
                - Realistic chance of winning
                - Potential revenue impact
                
                Format: Opportunity name | Score /10 | One line reason"""
            }
        ]
    )
    
    scores = response.content[0].text
    return {**state, "scores": [scores]}

def summariser(state: AgentState) -> AgentState:
    print("📝 Summariser is working...")
    
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are an executive business analyst.
                
                Company profile: {state['company_profile']}
                
                Opportunities researched:
                {state['opportunities'][0]}
                
                Scores and reasoning:
                {state['scores'][0]}
                
                Write a short executive brief (max 150 words) that:
                - Summarises the top opportunities
                - Highlights the best one to pursue first
                - Gives a clear recommended next action"""
            }
        ]
    )
    
    summary = response.content[0].text
    return {**state, "summary": summary}

def create_agent_graph():
    # Create the graph with our state definition
    graph = StateGraph(AgentState)
    
    # Add our three agents as nodes
    graph.add_node("researcher", researcher)
    graph.add_node("scorer", scorer)
    graph.add_node("summariser", summariser)
    
    # Define the flow: researcher -> scorer -> summariser -> END
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "scorer")
    graph.add_edge("scorer", "summariser")
    graph.add_edge("summariser", END)
    
    # Compile and return the runnable graph
    return graph.compile()

def run_agent(company_profile: str) -> AgentState:
    graph = create_agent_graph()
    
    initial_state = AgentState(
        company_profile=company_profile,
        opportunities=[],
        scores=[],
        summary=""
    )
    
    result = graph.invoke(initial_state)
    return result


