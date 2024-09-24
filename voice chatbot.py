import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3

def chatbot_response(message):
    # Define some simple rules for the chatbot
    if message.lower() == "hello":
        return "Hi there!"
    elif message.lower() == "how are you":
        return "I'm good, thank you!"
    elif message.lower() == "what is your name":
        return "I'm a chatbot. What's yours"
    elif message.lower() == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def process_text_to_speech(response):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1
    engine.say(response)
    engine.runAndWait()

def listen_for_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_message = recognizer.recognize_google(audio)
        print("You said:", user_message)
        return user_message
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_user_input():
    user_message = listen_for_voice_input()

    if user_message.strip() == "":
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_message + "\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

    bot_response = chatbot_response(user_message)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Chatbot: " + bot_response + "\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

    process_text_to_speech(bot_response)

def main():
    global chat_history

    root = tk.Tk()
    root.title("Voice Chatbot")
    root.configure(bg="#A020F0")
    root.geometry("800x500")
    chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20,bg="#880000", state=tk.DISABLED)
    chat_history.pack(padx=10, pady=10)

    listen_button = tk.Button(root, text="Listen", command=process_user_input,bg="blue",fg="yellow")
    listen_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
