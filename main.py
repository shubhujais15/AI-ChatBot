import pyautogui
import time
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Fetch the GEMINI_API_KEY from environment variables to authenticate with the generative AI model
api_key = os.getenv("GEMINI_API_KEY")
# Configure the API client with the API key
genai.configure(api_key=api_key)
# Initialize the generative AI model (gemini-1.5-flash) for generating responses
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to check if the last message in the chat history is from a specific sender
def is_last_msg_from_sender(chat_log, sender_name='write sender Name'):
    # Split the chat log to isolate the latest message (after "/2024]")
    message = chat_log.strip().split("/2024] ")[-1]
    # Check if the sender's name is in the message
    if sender_name in message:
        return True
    return False

# Clicking on the application window at specific coordinates to bring it to focus
pyautogui.click(1214, 1049)
time.sleep(1)

# Infinite loop to continuously monitor the chat
while True:
    # Simulate dragging the mouse to highlight the chat history area
    pyautogui.moveTo(764, 237)
    pyautogui.dragTo(1692, 928, duration=1.0, button='left')

    # Simulate the 'Ctrl + C' keyboard shortcut to copy the selected text (chat history)
    pyautogui.hotkey('ctrl', 'c')

    # Click on the application again to ensure it's focused
    pyautogui.click(1727, 918)
    time.sleep(3)

    # Paste the copied chat history from the clipboard
    chat_history = pyperclip.paste()

    # If the last message is from the sender, process the chat and generate a response
    if is_last_msg_from_sender(chat_history):
        # Prepare a prompt for the generative model to craft a response
        prompt = f""" 
        You are a person named Shubham, who speaks hindi as well as english . You are from India. you analyze the chat and respond like shubham with short and genuine text.
        {chat_history}
        """
        # Generate a response from the model using the prompt
        response = model.generate_content(prompt)

        # Copy the generated response text to the clipboard
        pyperclip.copy(response.text)

        # Simulate clicking on the chat input area to focus on it
        pyautogui.click(877, 970)
        time.sleep(2)

        # Simulate the 'Ctrl + V' keyboard shortcut to paste the response into the chat
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)

        # Simulate pressing 'Enter' to send the generated response
        pyautogui.press('enter')
