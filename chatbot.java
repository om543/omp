import streamlit as st
from data import data

st.title("Chatbot")

msg = st.text_input("You:")

if msg:
    st.write("Bot:", data.get(msg.lower(), "I don't understand"))
