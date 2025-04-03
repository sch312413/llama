import os
import time
import streamlit as st
import google.generativeai as genai

st.title("AI Chat Bot")

model_options = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-1.5-pro"
]
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
selected_model = st.selectbox("Choose Gemini Model", options=model_options, index=2)
model = genai.GenerativeModel(selected_model)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Enter your question ..."):
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        history = ""
        for msg in st.session_state.messages:
            role = "User" if msg["role"] == 'user' else 'Assistant'
            history += f"{role}: {msg['content']}\n"

        prompt = history + f"User: {query}\nAssistant:"

        response_obj = model.generate_content(prompt)

        if response_obj.parts:
            response = "".join([part.text for part in response_obj.parts])
        else:
            response = (
                "Response blocked: The model detected potentially copyrighted content"
                "and did not return any output. Please try rephrasing your prompt."
        )

        full_response = ""
        for char in response:
            full_response += char
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.005)
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})