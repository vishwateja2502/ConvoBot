import json
import os
import streamlit as st
import requests

st.write("# ConvoBot: Smart Conversations 〽️")

# Sidebar configuration for model selection and streaming option
model = st.sidebar.selectbox("Model", ["phi3"])
streaming = st.sidebar.selectbox("Streaming", [True, False])
BACKEND_URL = "http://localhost:11434/api/generate"

# Custom styling for chat messages
st.markdown("""
    <style>
        .user-message {
            background-color: #A2DFF7; /* Light Blue */
            border-radius: 15px;
            padding: 12px;
            margin: 8px 0;
            font-family: 'Arial', sans-serif;
            color: #1C4C72; /* Dark blue text */
            max-width: 80%;
            word-wrap: break-word;
        }
        .assistant-message {
            background-color: #3A8DFF; /* Bright Blue */
            color: white;
            border-radius: 15px;
            padding: 12px;
            margin: 8px 0;
            font-family: 'Arial', sans-serif;
            max-width: 80%;
            word-wrap: break-word;
        }
        .stSpinner {
            font-size: 1.5em;
            color: #3A8DFF;
        }
        .footer {
            position: absolute;
            bottom: -600px;  /* Adjust bottom to move further down */
            left: 15px;
            font-size: 14px;
            color: #555;
            font-family: 'Arial', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Add your name to the bottom of the sidebar
st.sidebar.markdown("<div class='footer'>Created by Vishwa Teja Rachamalla</div>", unsafe_allow_html=True)

# Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the chat history from session state (user and assistant messages)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# Capture user input
prompt = st.chat_input("Type a message...")

if prompt:
    # Append the user's message to the chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Display the user's message in the chat window
    with st.chat_message("user"):
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    # Handle streaming response from the backend
    if streaming:
        res = requests.post(f"{BACKEND_URL}/", 
                            json={
                                "model": model,
                                "prompt": prompt
                            },
                            stream=True)

        with st.chat_message("assistant"):
            full_response = ""
            message_placeholder = st.empty()

            # Stream the response and update the chat message in real-time
            for line in res.iter_lines():
                if line:
                    data = json.loads(line)
                    if data["done"]:
                        break
                    full_response += data["response"]
                    message_placeholder.markdown(f'<div class="assistant-message">{full_response}</div>', unsafe_allow_html=True)

            # Once streaming is done, add the full response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": full_response})

    # Handle non-streaming response from the backend
    else:
        with st.spinner("Thinking...💭"):
            res = requests.post(f"{BACKEND_URL}/", 
                                json={
                                    "model": model,
                                    "prompt": prompt,
                                    "stream": streaming
                                }).json()
            assistant_response = res.get("response", "")
            
            # Append the assistant's response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

            # Display the assistant's response in the chat window
            with st.chat_message("assistant"):
                st.markdown(f'<div class="assistant-message">{assistant_response}</div>', unsafe_allow_html=True)
