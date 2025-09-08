import os
import streamlit as st
from openai import OpenAI

os.environ["GROQ_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="Nik ChatApp", layout="centered")
st.title("💬 Nik ChatApp")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for role, content in st.session_state["messages"]:
    with st.chat_message(role):
        st.markdown(content)

if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": r, "content": c} for r, c in st.session_state["messages"]]
    )

    reply = response.choices[0].message.content
    st.session_state["messages"].append(("assistant", reply))

    with st.chat_message("assistant"):
        st.markdown(reply)
