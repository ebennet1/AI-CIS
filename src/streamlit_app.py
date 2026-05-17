import streamlit as st
from langchain_openai import ChatOpenAI

st.title("AI Chief of Staff")

meeting_notes = st.text_area("Paste meeting notes")

if st.button("Generate Summary"):
    model = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
    Summarize the following meeting notes.

    Include:
    - Executive Summary
    - Risks
    - Action Items
    - Decisions

    Notes:
    {meeting_notes}
    """

    response = model.invoke(prompt)

    st.write(response.content)
