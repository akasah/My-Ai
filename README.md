# Voice-Controlled Assistant (Alexa)

This Python script creates a simple voice-controlled assistant (Jarvis) using `pyttsx3` for text-to-speech and `speech_recognition` for speech recognition. Jarvis can open specific websites based on voice commands and respond to basic interactions.

## Requirements

- Python 3.x
- Install required libraries:
  ```bash
  pip install pyttsx3 speech_recognition
How It Works
Functionality
Voice Input:

Jarvis listens for commands after a greeting prompt.
Commands Supported:

Greetings: Responds to "hello".
Farewells: Responds to "bye".
Opening Websites: Recognizes keywords to open Google, YouTube, Instagram, and LinkedIn.
Speech Recognition:

Utilizes speech_recognition to recognize voice commands from the microphone.
Adjusts for ambient noise before listening.
Text-to-Speech:

Uses pyttsx3 to convert text responses into spoken words.
Usage
Running the Script:

Open a terminal or command prompt.
Navigate to the directory containing main.py.
Run the script:
bash
Copy code
python main.py
Interaction:

Jarvis will greet you and listen for your commands.
Speak clearly into the microphone:
Say "hello" for a greeting.
Say "bye" to exit Jarvis.
Say "open Google", "open YouTube", "open Instagram", or "open LinkedIn" to open the respective websites.
Ending Interaction:

To end the session, say "bye" and Jarvis will bid farewell.
Notes
Customize the open_website() function in main.py to add more websites or functionalities based on your needs.
Ensure your microphone is connected and functioning properly for accurate speech recognition.
