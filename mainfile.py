import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import webbrowser
import pyjokes
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = listener.listen(source)
    try:
        print("Recognizing...")
        audio = listener.recognize_google(audio)
        print("user said: "+audio)
    except Exception as e:
        # speak("I am unable to understand..can you please repeat it again")
        # print("I am unable to understand..can you please repeat it again")
        return "Nothing"
    return audio


def wish():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")
    elif hour <= 16:
        speak("Good Afternoon")
        print("Good Afternoon")
    elif hour <= 19:
        speak("Good Evening")
    else:
        speak("Nighty Night")
        print("Nighty Night")

    print("Hello i am Alexa. Please tell me how can i help you")
    speak("Hello i am Alexa. Please tell me how can i help you")
    # take_command()


wish()
while True:
    query = take_command().lower()
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif 'play' in query:
        song = query.replace('play', "")
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(time)
        print(time)
    elif "joke" in query:
        result = pyjokes.get_joke()
        print(result)
        speak(result)
# wish()
