# Voice-chatbot

# Voice Chat Bot

This is a simple voice chat bot built using Python. The bot can recognize speech, process the input, and respond with synthesized speech.

## Features

- Speech recognition using `speech_recognition`
- Text-to-speech using `pyttsx3`
- Natural language processing using `nltk`
- Simple and extensible codebase

## Requirements

- Python 3.6+
- `speech_recognition`
- `pyttsx3`
- `nltk`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/voice-chat-bot.git
    cd voice-chat-bot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

## Usage

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Speak into your microphone when prompted. The bot will recognize your speech, process it, and respond with synthesized speech.

## Example Code

Here's a basic example of how the bot works:

```python
import speech_recognition as sr
import pyttsx3
import nltk

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None

def respond(text):
    response = f"You said: {text}"
    tts_engine.say(response)
    tts_engine.runAndWait()

if __name__ == "__main__":
    while True:
        text = recognize_speech()
        if text:
            respond(text)


You can customize this `README.md` file to better fit your project's specifics. If you need any more details or help with the code, feel free to ask!
