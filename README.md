# 💬 NLPR Project – Part 2: Mental Health Chatbot (AI Psychologist) with Rasa + GPT-4o + Streamlit

![Python](https://img.shields.io/badge/Built%20with-Rasa%20%7C%20GPT--4o%20%7C%20Streamlit-blue)
![Rasa](https://img.shields.io/badge/Framework-Rasa-orange?logo=rasa)
![Chatbot](https://img.shields.io/badge/Domain-Mental%20Health%20Support-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project implements an **AI Psychologist chatbot** using **Rasa** for intent handling, **GPT-4o** (via OpenAI API) for empathetic response generation, and **Streamlit** for a user-friendly web interface. It is designed to offer **emotional support**, engage in open-ended mental health conversations, and simulate a safe space for users in need.

---

## 🧠 Project Objectives

- Recognize user intent and emotional cues through NLP
- Respond to negative emotions with comforting, human-like messages
- Combine rule-based conversation with GPT-4o intelligence
- Store chat history to monitor recurring emotional struggles
- Provide a polished and accessible user interface

---

## 💬 Chatbot Features

### 🤖 Intent Recognition (via Rasa)
- `greet`, `goodbye`, `affirm`, `deny`
- `mood_great`, `mood_unhappy` – triggers emotional support flow
- `ask_chatbot` – open-ended guidance requests
- `bot_challenge` – questions about the AI itself

### 💡 GPT-4o Integration via Custom Action
- The action server (`actions.py`) sends user messages to GPT-4o with a system role:  
  _"You are a psychologist AI here to offer emotional support."_
- GPT generates context-sensitive, empathetic replies

### 🌐 Streamlit Web App
- Simple chat interface via `chatbot_ui.py`
- Sends user messages to Rasa backend and displays GPT-powered responses
- Clean and accessible for mobile or desktop use

### 💾 Optional MySQL Logging
- Chat history can be stored to identify repeat users needing help
- Enables long-term monitoring or alerting systems

---

## 📸 Sample Use Case

> **User**: I'm feeling anxious and overwhelmed.  
> **Bot**: I'm really sorry you're feeling this way. It's okay to experience tough emotions. Would you like to talk more about what’s on your mind?

---

## 🔧 Setup Instructions

### 1. Create and activate your environment
```bash
conda create -n rasa-chatbot python=3.8
conda activate rasa-chatbot
```

### 2. Install requirements
```bash
pip install rasa streamlit openai mysql-connector-python
```

### 3. Train the Rasa model
```bash
rasa train
```

### 4. Start Rasa and the custom action server
```bash
rasa run actions     # Terminal 1
rasa shell           # OR: rasa run --enable-api   (Terminal 2)
```

### 5. Launch the Streamlit frontend
```bash
streamlit run chatbot_ui.py
```

---

## 📈 Project Highlights (from Presentation)

- Connected GPT-4o with custom prompts tailored for emotional support
- Created intents and stories for mental health situations
- MySQL integration for chat logs (optional)
- Built and tested Streamlit UI with users (family/friends)
- Achieved natural, comforting responses with minimal rule scripting

---

## ✅ Future Improvements

- Add sentiment analysis to guide GPT tone
- Build user authentication and secure log storage
- Include journaling and mental health check-ins
- Expand intent coverage and multilingual support

---

## 👤 Author

**Moanish Ashok Kumar**  
Applied AI Student  
🔗 [LinkedIn](https://www.linkedin.com/in/moanish-ashok-kumar-086978272/)

---

> ⚠️ _Note: This chatbot is not a replacement for professional therapy. It is designed as a first-level emotional support tool for light-to-moderate conversation._
