import os
import asyncio
from dotenv import load_dotenv

# For Streamlit secrets (works only when running inside Streamlit)
try:
    import streamlit as st
except ImportError:
    st = None

import arxiv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

# ------------------------------------------------------
# Load environment variables / Streamlit secrets
# ------------------------------------------------------
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY") or (st.secrets["GROQ_API_KEY"] if st and "GROQ_API_KEY" in st.secrets else None)
if not groq_key:
    raise RuntimeError("GROQ_API_KEY not found in .env or Streamlit secrets")

# ------------------------------------------------------
# Build a team of agents for literature review
# ------------------------------------------------------
def build_team(model: str = "llama-3.3-70b-versatile") -> RoundRobinGroupChat:
    client = OpenAIChatCompletionClient(
        model=model,
        api_key=groq_key,
        base_url="https://api.groq.com/openai/v1",
        include_name_in_message=True,
        model_info=ModelInfo(
            vision=False,
            function_calling=False,
            json_output=False,
            family="llama",
            structured_output=False
        )
    )

    assistant = AssistantAgent(
        name='ResearchAssistant',
        description='Summarizes and critiques academic papers.',
        model_client=client,
        system_message='You help with literature reviews.'
    )

    reviewer = AssistantAgent(
        name='PaperReviewer',
        description='Reviews and critiques research papers.',
        model_client=client,
        system_message='You provide constructive critiques of research.'
    )

    user_proxy = UserProxyAgent(
        name='UserProxy',
        description='Represents the user in the conversation.',
        input_func=input
    )

    return RoundRobinGroupChat([assistant, reviewer, user_proxy])

# ------------------------------------------------------
# Fetch papers from arXiv
# ------------------------------------------------------
def fetch_papers(query: str, max_results: int = 5):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id,
            "published": result.published
        })
    return papers

# ------------------------------------------------------
# Run the literature review (async generator)
# ------------------------------------------------------
async def run_litrev(topic: str, num_papers: int = 5):
    papers = fetch_papers(topic, max_results=num_papers)
    if not papers:
        yield "ResearchAssistant: No papers found."
        return

    team = build_team()
    prompt = "Summarize and critique these papers:\n\n"
    for i, p in enumerate(papers, 1):
        prompt += (
            f"Paper {i}:\n"
            f"Title: {p['title']}\n"
            f"URL: {p['url']}\n"
            f"Published: {p['published']}\n"
            f"Summary: {p['summary']}\n\n"
        )

    async for message in team.run_stream(task=prompt):
        yield message

# ------------------------------------------------------
# Demo runner (optional local test)
# ------------------------------------------------------
async def _demo():
    async for msg in run_litrev("Artificial Intelligence", num_papers=5):
        print(msg)

if __name__ == "__main__":
    asyncio.run(_demo())
