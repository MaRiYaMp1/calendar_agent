import streamlit as st
import requests

st.title("📅 Booking Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

def send(msg):
    res = requests.post("http://localhost:8000/chat", json={"message": msg})
    return res.json()["response"]

user_input = st.text_input("You")
if st.button("Send") and user_input:
    st.session_state.history.append(("user", user_input))
    bot_reply = send(user_input)
    st.session_state.history.append(("assistant", bot_reply))

for role, msg in st.session_state.history:
    st.markdown(f"**{role}**: {msg}")
