import streamlit as st
import requests
import time
from datetime import datetime

# Rasa API endpoint
RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

# Custom Styling with Streamlit CSS
st.markdown(
    """
    <style>
        /* Set background color */
        body {
            background-color: #F4F6F7;
        }

        /* Chat messages formatting */
        .user-message, .bot-message {
            padding: 12px;
            border-radius: 10px;
            max-width: 80%;
            margin-bottom: 10px;
        }

        /* User message styling */
        .user-message {
            background-color: #DCF8C6;
            align-self: flex-end;
            text-align: right;
        }

        /* Bot message styling */
        .bot-message {
            background-color: #E8EAF6;
            align-self: flex-start;
        }

        /* Chat message container */
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title with emoji
st.title("🧠 AI Psychologist Chatbot 🤖")

# Clear Chat Button
if st.button("🗑 Clear Chat"):
    st.session_state.messages = []

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with proper formatting and timestamps
for message in st.session_state.messages:
    timestamp = datetime.now().strftime("%I:%M %p")  # Get current time
    with st.chat_message(message["role"]):
        st.markdown(f"{message['content']}  \n*{timestamp}*", unsafe_allow_html=True)

# User input box
user_input = st.chat_input("📝 Type your message...")

if user_input:
    # Store user message with timestamp
    timestamp = datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": timestamp})
    
    with st.chat_message("user"):
        st.markdown(f"{user_input}  \n*{timestamp}*", unsafe_allow_html=True)

    # Show "typing..." indicator before the response
    with st.spinner("🤖 Typing..."):
        time.sleep(1.5)  # Short delay to mimic human typing

        try:
            # Send request to Rasa API
            response = requests.post(RASA_API_URL, json={"sender": "user", "message": user_input}, timeout=60)

            # Extract bot response safely
            if response.status_code == 200 and response.json():
                bot_reply = response.json()[0].get("text", "I'm here for you. Can you tell me more?")
            else:
                bot_reply = "I'm here for you. Can you tell me more?"

        except requests.exceptions.RequestException as e:
            bot_reply = "🚨 Sorry, I'm experiencing connection issues. Please try again later."
            print(f"Error: {e}")  # Logs the error in the terminal

    # Ensure proper formatting for chatbot response
    formatted_reply = bot_reply.replace("\n", " ")  # Remove unwanted line breaks

    # Store bot response with timestamp
    timestamp = datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({"role": "assistant", "content": formatted_reply, "timestamp": timestamp})

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(f"{formatted_reply}  \n*{timestamp}*", unsafe_allow_html=True)