import openai
import streamlit as st
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Streamlit UI
st.title("Customer Support Chatbot")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", placeholder="Type your question here...")

# Function to get response from OpenAI
def get_openai_response(messages, model="gpt-3.5-turbo", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"].strip()

# Handle user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    assistant_response = get_openai_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**AI:** {message['content']}")
