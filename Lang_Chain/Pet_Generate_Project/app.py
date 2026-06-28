import streamlit as st
from main import generate_pet_name 
from agent_helper import search_wikipedia  # <-- Import your new Agent function

# 1. Main Page Setup
st.set_page_config(page_title="AI Helper Hub", page_icon="🤖")
st.title("🤖 My Multi-Tool AI Hub")

# 2. Creating Tabs
tab1, tab2 = st.tabs(["🐾 Pet Names", "📖 Wikipedia Search"])

# --- TAB 1: Pet Name Generator ---
with tab1:
    st.header("Pet Name Generator")
    animal_type = st.text_input("What is your pet?", key="pet_input")
    
    if st.button("Generate Names"):
        if animal_type:
            with st.spinner("AI is thinking..."):
                response = generate_pet_name(animal_type)
                st.success(f"Suggested names for {animal_type}:")
                st.write(response)
        else:
            st.warning("Please type an animal name!")

# --- TAB 2: Wikipedia Agent ---
with tab2:
    st.header("AI Wikipedia Agent")
    wiki_query = st.text_input("What do you want to learn about?", key="wiki_input")
    
    if st.button("Ask Agent"):
        if wiki_query:
            with st.spinner("Agent is searching Wikipedia..."):
                # This calls your agent_helper.py function!
                result = search_wikipedia(wiki_query)
                st.info("Agent Found This:")
                st.write(result)
        else:
            st.warning("Please type a topic to search!")
