import streamlit as st
from agents.travel_agent import run_agent

st.set_page_config(page_title="AI Travel Assistant")

st.title("AI Travel Assistant")

query = st.text_input("Ask me about travel plans:")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        response = run_agent(query)
    st.write("### Recommendation")
    st.write(response)
