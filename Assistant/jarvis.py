


import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir, Please tell me how may I help you")

def takeCommand():
    '''
    IT takes microphines input from the user and return string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please ...")
        return "None"
    return query



if __name__=="__main__":
    speak("Welcome to this amazing world!")
    wishMe()
    takeCommand()
    if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('According to Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("in Wikipedia")
            print(results)
            speak(results) 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")
            
        # elif 'play my music' in query:
        #     music_dir ="https://www.linkedin.com/feed/"
        # songs = os.listdir(music_dir)
        # print(songs)
        # os.startfile(os.path.join(music_dir,songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        elif 'open download folder' in query:
            downloadPath="C:\\Users\\Varun\\Downloads"
            os.startfile(downloadPath)
        elif 'open project folder' in query:
            projectPath="E:\\project"
            os.startfile(projectPath)
        elif 'open vs code' in query:
            vscodePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(vscodePath)
        
