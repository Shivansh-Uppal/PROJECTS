import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import googleapiclient
import monotonic
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour=int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12: 
     speak("good morning!")
    elif hour>=12 and hour<=18: 
        speak("good afternoon!")
    else: 
        speak("good evening!")
        
    speak("I am DAVID sir. Please tell me how can i help you !")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold= 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        
    try: 
        print("recognizing...")
        query=r.recognize_google(audio)
        print(f"user said:{query}\n")
        
    except Exception as e: 
      
        print("say that again please...")
        return "None"
    return query
        
def sendEmail(to,content): 
    pass
#need to enable less secure apps till then not working
    
if __name__ == "__main__":
    wishMe()
    while True:
     query=takeCommand().lower()
     
     
     if 'wikipedia' in query : 
         speak('searching wikipedia...')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("according to wikipeddia")
         print(results)
         speak(results)
         
     elif "open youtube" in query :
         webbrowser.open("youtube.com")
         
     elif "open google" in query :
         webbrowser.open("google.com")
         
     elif "open stack overflow" in query :
         webbrowser.open("stackoverflow.com")
         
     elif "time" in query: 
         strtime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"SIR,THE TIME IS {strtime}")
         
     elif "code" in query:
         codepath=r"C:\Users\shivansh uppal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
         os.startfile(codepath)
         
         
     elif "mail" in query:
         #need to enable less secure apps till then not working
         try: 
             speak("what should i say ?")
             content=takeCommand()
             to = "shivanshway@gmail.com"
             sendEmail(to,content)
             speak("email is sent")
             
         except Exception as e: 
             print(e)
             speak("sorry sir, email is not sent ")
             
        
         
    
    

