import asyncio
import json
import streamlit as st
from autogen_backend import run_litrev
from autogen_agentchat.messages import TextMessage

st.set_page_config(page_title="Literature Review Assistant", page_icon="📚")
st.title("📚 Literature Review Assistant")

query = st.text_input("Research topic", placeholder="e.g., Explainable AI in healthcare")
n_papers = st.slider("Number of papers", 1, 10, 5)

if st.button("Search") and query:

    async def _runner():
        chat_placeholder = st.container()
        
        async for frame in run_litrev(query, num_papers=n_papers):
            if isinstance(frame, TextMessage):
                role = getattr(frame, "name", "assistant").lower()
                content = frame.content
            else:
                role = "assistant"
                content = str(frame)

            with chat_placeholder:
                with st.chat_message("assistant"):
                    try:
                        data = json.loads(content)
                        if isinstance(data, list):
                            st.subheader(f"📄 Selected Papers ({len(data)})")
                            for paper in data:
                                st.markdown(
                                    f"**Title:** {paper.get('title')}\n\n"
                                    f"**Authors:** {', '.join(paper.get('authors', []))}\n\n"
                                    f"**Published:** {paper.get('published')}\n\n"
                                    f"**Summary:** {paper.get('summary')}\n\n"
                                    f"[PDF Link]({paper.get('pdf_url')})"
                                )
                        elif isinstance(data, dict):
                            st.subheader(f"📝 {data.get('title', 'Literature Review')}")
                            st.markdown(data.get('content', ''))
                        else:
                            st.markdown(content)
                    except json.JSONDecodeError:
                        st.markdown(f"**{role.capitalize()}**: {content}")

    with st.spinner("Working…"):
        try:
            asyncio.run(_runner())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(_runner())

    st.success("Review complete 🎉")
