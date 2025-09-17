import streamlit as st
from agents.travel_agent import plan_trip

st.set_page_config(page_title="AI Travel Assistant")
st.title("AI Travel Assistant")

st.write("Describe your travel preferences and I'll suggest destinations, weather, and events.")

user_input = st.text_area("Your travel query:", placeholder="E.g., I want a beach vacation in December")

if st.button("Plan my trip") and user_input:
    with st.spinner("Planning your trip..."):
        try:
            result = plan_trip(user_input)
        except Exception as e:
            result = f"Error: {e}"
    st.write("### Recommendations")
    st.write(result)
