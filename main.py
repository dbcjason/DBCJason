import streamlit as st

st.set_page_config(page_title="Dynasty Fantasy Basketball App", page_icon="🏀", layout="wide")

st.title("Welcome to the jAIson Dynasty Trade Machine!")
st.write("Select a tool from the sidebar to get started.")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.page_link("main.py", label="🏠 Home", icon="🏡")
st.sidebar.page_link("pages/trade_machine.py", label="🔄 Trade Machine")
st.sidebar.page_link("pages/peak_projections.py", label="📈 Peak Projections")
st.sidebar.page_link("pages/dynasty_rankings.py", label="📊 Dynasty Rankings")
