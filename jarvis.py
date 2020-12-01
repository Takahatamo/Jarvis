import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# Sites
youTube = 'https://www.youtube.com/'
google = 'https://www.google.ca/'
stackOverFlow = 'https://stackoverflow.com/'
gitHub = 'https://github.com/'
discord = 'https://discord.com/channels/@me'

# Chrome Path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I'm Jarvis! How may I help you?")


def takeCommand():
    '''
# takes mic input from the user
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open(youTube)
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open(google)
            speak("Opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open(stackOverFlow)
            speak("Opening StackOverFlow")

        elif 'open discord' in query:
            webbrowser.get(chrome_path).open(discord)
            speak("Opening Discord")

        elif 'open github' in query:
            webbrowser.get(chrome_path).open(gitHub)
            speak("Opening GitHub")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
