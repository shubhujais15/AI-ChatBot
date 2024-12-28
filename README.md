# 🧠 AI ChatBot Automation 🚀  

This project brings conversational automation to life! Using the **Gemini AI model**, it monitors chat history, identifies messages from a specific sender, and generates dynamic, human-like responses with a blend of **Hindi** and **English**.

---

## 📑 Table of Contents  
- [✨ Overview](#-overview)  
- [🌟 Features](#-features)  
- [⚙️ Installation](#%EF%B8%8F-installation)  
- [📝 Usage](#-usage)  
- [📦 Dependencies](#-dependencies)  
- [🔧 Configuration](#-configuration)  
- [🔄 Execution Flow](#-execution-flow)  

---

## ✨ Overview  

The **AI ChatBot Automation** is a powerful script designed to take over your chat conversations in real-time. It interacts with incoming messages, detects sender-specific inputs, and generates **AI-driven responses** using the **Gemini AI model** (`gemini-1.5-flash`).  

> ⚡ **Key Highlight**: Seamlessly blends Hindi and English for natural interactions, making every conversation feel personal and engaging!  

---

## 🌟 Features  

- 💬 **Automated Chat Replies**:  
  Effortlessly monitor incoming messages and send intelligent, context-aware responses.  

- 🤖 **AI-Driven Conversations**:  
  Powered by **Gemini AI**, ensuring human-like responses tailored to the chat context.  

- 🎨 **GUI Automation**:  
  Interacts with chat apps using **pyautogui** for mouse clicks and keyboard input.  

- 🌍 **Multilingual Support**:  
  Communicates fluently in **Hindi** and **English** for a personalized touch.  

---

## ⚙️ Installation  

Follow these simple steps to get started:  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/shubhujais15/AI-ChatBot.git  
   cd AI-ChatBot  
   ```  

2. **Create a Virtual Environment** (optional but recommended):  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**:  
   Ensure **Python 3.6+** is installed, then run:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up Environment Variables**:  
   - Create a `.env` file in the root directory.  
   - Add your **Gemini API key** as shown below:  
     ```  
     GEMINI_API_KEY=your_api_key_here  
     ```  

---

## 📝 Usage  

1. **Start the Script**:  
   Launch the chatbot automation:  
   ```bash  
   python main.py  
   ```  

2. **Watch It in Action**:  
   - The bot will monitor your chat for messages from a specific sender (default: **"Sender_Name"**).  
   - When a new message is detected, it generates an intelligent response and sends it.  

3. **Stop the Script**:  
   Hit `Ctrl + C` to terminate the script.  

---

## 📦 Dependencies  

The project uses these Python libraries:  

- 🖱️ **pyautogui**: For GUI automation (mouse & keyboard control).  
- 📋 **pyperclip**: For clipboard management (copy-paste operations).  
- 🌍 **python-dotenv**: To load environment variables.  
- 🤖 **google.generativeai**: To interact with the Gemini AI model.  

---

## 🔧 Configuration  

### Sender Name  
Update the `is_last_msg_from_sender` function to customize the sender’s name (default: **"Sender_Name"**).  

### Gemini API Key  
Ensure the `.env` file contains your **Gemini API key** for authentication.  

### Chat Application Compatibility  
The script relies on clipboard operations to monitor chat messages. Make sure your chat app supports this functionality!  

---

## 🔄 Execution Flow  

🌀 **Here’s How It Works**:  
1. The script starts by initializing necessary libraries and configuring the AI model.  
2. It continuously monitors the chat window by:  
   - Simulating **mouse clicks** to select the chat area.  
   - **Copying chat history** to the clipboard.  
   - Checking if the last message is from the designated sender.  
3. When a new message is detected:  
   - The chat history is sent to the Gemini AI model for processing.  
   - The generated reply is copied to the clipboard.  
   - The bot pastes the reply into the chat input and sends it.  
4. The cycle repeats until the script is stopped.  

---

> 🌟 **Pro Tip**: This bot is perfect for automating replies in personal or professional conversations, ensuring you never miss a beat!  

🎉 **Happy Chatting!**  
