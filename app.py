import streamlit as st
from chatbot.config import ACTIVE_ENV_FILE, ENV_FILE, LEGACY_ENV_FILE, get_api_key
from chatbot.service import ask_cohere

st.title("My AI Chatbot")
st.write("Ask me anything!")

api_key = get_api_key()
if ACTIVE_ENV_FILE == LEGACY_ENV_FILE:
    st.warning(
        "Your .env is inside the virtual environment. Move it beside app.py "
        f"for future runs: {ENV_FILE}"
    )

if api_key is None:
    st.warning(f"Set COHERE_API_KEY in this file to get answers: {ENV_FILE}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your question..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    if api_key is None:
        st.error("Your question was not sent. Add COHERE_API_KEY to the .env file, then try again.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = ask_cohere(
                        api_key,
                        st.session_state.messages,
                    )
                    st.write(answer)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )

                except Exception as e:
                    st.error(f"Error: {e}")