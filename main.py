import win32com.client
import speech_recognition as sr
import datetime
import webbrowser
import os
from google import genai

# ---------------- GEMINI SETUP ----------------
client = genai.Client(api_key=os.getenv("Your API KEY"))

# Voice engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower()
    except:
        return "none"


# -------- AI RESPONSE FUNCTION --------
def ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return "Sorry, I am having trouble understanding right now."


# ---------------- START ----------------
speak("Hello, I am Jarvis AI. How can I help you?")

while True:
    query = takeCommand()

    if query == "none":
        continue

    # Open websites
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"]
    ]

    for site in sites:
        if f"open {site[0]}" in query:
            speak(f"Opening {site[0]}")
            webbrowser.open(site[1])
            break

    if query == "exit":
        speak("Goodbye")
        break

    elif "time" in query:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time_now}")

    elif "open vs code" in query:
        speak("Opening Visual Studio Code")
        os.startfile(r"C:\Users\Public\Desktop\Visual Studio Code.lnk")

    else:
        reply = ai_response(query)
        print("Jarvis:", reply)
        speak(reply)