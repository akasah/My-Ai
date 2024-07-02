import pyttsx3
import speech_recognition as sr
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, can you repeat once")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            speak("Sorry, my speech service is down.")
            return None

def open_website(command):
    if "google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "instagram" in command.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "linkedin" in command.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/in/akash1207/")
    else:
        speak("Sorry, I can only open Google, YouTube, Instagram, and LinkedIn right now.")

def jarvis():
    speak("Hello,Akash my master ,how can I HELP you?")
    while True:
        command = listen()
        if command:
            if "hello" in command.lower():
                speak("Hello! How are you?")
            elif "bye" in command.lower():
                speak("GoodBye ! HAve a nice nay")
                break
            elif "open" in command.lower():
                open_website(command)
            else:
                speak("I am sorry, I don't understand that command.")

if __name__ == "__main__":
    jarvis()
