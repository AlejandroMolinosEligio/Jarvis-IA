

import speech_recognition as sr
import pyttsx3 as p
import pywhatkit
import webbrowser
import time
import datetime
import subprocess
import json
import requests
import wikipedia
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

### PROPIEDADES JARVIS Y NAVEGADOR

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",150)
browser = webbrowser.os.path.join(webbrowser.os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                                "BraveSoftware\\Brave-Browser\\Application\\BRAVE.EXE")

webbrowser.register('Brave', None, webbrowser.BackgroundBrowser(browser),preferred=True)

browser = webbrowser.os.path.join(webbrowser.os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                                "Mozilla Firefox\\FIREFOX.EXE")

webbrowser.register('Firefox', None, webbrowser.BackgroundBrowser(browser))

### METODOS

def whatsapp():

    subprocess.call("C:\\Users\\aleja\\Desktop\\Jarvis\\whatsapp.bat")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello, good Morning")
        speak("Hello,good Morning")
    elif hour>=12 and hour<18:
        print("Hello, good Afternoon")
        speak("Hello, good Afternoon")
    else:
        print("Hello, good Evening")
        speak("Hello, good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening instrucction...")
        audio = r.listen(source)
        try:
            recognised_audio = r.recognize_google(audio)
            print("User said: "+recognised_audio)
        except Exception as e:
            speak("Sorry i didn't recognized it")
            recognised_audio2 = takeCommand()
            return recognised_audio2
        return recognised_audio

def takeCommandJ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start conversation...")
        audio = r.listen(source)
        try:
            recognised_audio = r.recognize_google(audio)
            print("User said: "+recognised_audio)
        except Exception as e:
        #    speak("You didn't say the magic word")
            return "None"
        return recognised_audio

def takeCommandNO():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            recognised_audio = r.recognize_google(audio)
        except Exception as e:
            return "None"
        return recognised_audio
            

### PROGRAMA

print('''
#######################################################################################
###################        _         _______      _______  _____    ###################
###################       | |  /\   |  __ \ \    / /_   _|/ ____|   ###################
###################       | | /  \  | |__) \ \  / /  | | | (___     ###################
###################   _   | |/ /\ \ |  _  / \ \/ /   | |  \___ \    ###################
###################  | |__| / ____ \| | \ \  \  /   _| |_ ____) |   ###################
###################   \____/_/    \_\_|  \_\  \/   |_____|_____/    ###################
###################                                                 ###################
#######################################################################################
                       
                                    %&&&&&&&&&&&&.            
                               &&&&( &&*    &&*/#&&&         
                             &&#     &&&   #&&     (&&&      
                           &&&&%(,,******//////////(&&&&     
                          &&&&&%&&&*,,,,,,,,,,,,/&&&%&&&&    
                         ,&& .&&(  #&(        (&(  (&( (&&   
                         %&%   (&&. .&&/    *&%   &%   (&&   
                          &&&&&&&&&(  (&&  #&/  (&%&&&&&&@   
                          &&%     (&&.  (&&(   &&*    (&&    
                           (&&/ (&&&&&( /&&( (&%&&&/ %&&     
                             &&&&#   .&&(&&(%#    (&&&       
                                &&&&(* %&&&&(.#%&&&(         
                                    ,&&&&&&&&&(                                         

                                            ''')
speak("Talk to me, i'm Jarvis your AI")
wishMe()
start = ['hey','jarvis', 'Jarvis', 'hi', 'good morning', 'good night']

if __name__=='__main__':

    speak("Tell me, how can i help you?")
    boo = True
    boo2 = False
    while True:
        
        if boo:
            jarvis = takeCommandJ().lower()
       
        if 'hey' in jarvis:
            if boo:
                speak("Yes sir?")
            statement = takeCommand().lower()
            if statement==0:
                continue

            elif "bye" in statement:
                speak("Goodnight sir...")
                print("Shutting down")
                break

            if 'youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                boo2 = True
            
            if 'university' in statement:
                webbrowser.open("ev.us.es",0,True)
                speak("University is open now")
                boo2 = True
                

            if 'netflix' in statement:
                webbrowser.open("netflix.com", 0, True)
                speak("Netflix is open now")
                boo2 = True

            if 'mail' in statement:
                webbrowser.open("www.gmail.com",0,True)
                speak("Google Mail open now")
                boo2 = True
                

            if 'calendar' in statement:
                webbrowser.open("https://calendar.google.com/",0,True)
                speak("Calendar is open now")
                boo2 = True

            if 'news' in statement:
                webbrowser.open("https://www.elmundo.es/",0,True)
                webbrowser.open("https://www.abc.es/",0,True)
                webbrowser.open("https://elpais.com/",0,True)
                speak("Ready to read the headlines")
                boo2 = True
            
            if 'spotify' in statement:
                subprocess.call(["C:\\Users\\aleja\\Desktop\\Jarvis\\spotify.bat"])
                speak("Spotify is opened")
                boo2 = True

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
                print(strTime)
                boo2 = True

            elif 'portrait mode' in statement:
                webbrowser.open("https://www.youtube.com/watch?v=ooCnP_s0K6s&list=PLDzHtjB3y01sQzY18ReyiHdL-FpVvRKmJ&index=1",0,True)
                boo2 = True

            elif 'search'  in statement:
                speak("What do you wanna search?")
                statement = takeCommand().lower()
                statement = statement.replace("search", "")
                print(statement)
                webbrowser.open("https://www.google.com/search?q="+statement,0,True)
                boo2 = True
            
            elif 'browser' in statement:
                print(webbrowser._browsers)
                boo2 = True

            elif 'whatsapp' in statement:
                whatsapp()
                boo2 = True

            elif 'play' in statement:
                music = statement.replace('play','')
                speak('Playing '+music)
                pywhatkit.playonyt(music)
                boo2 = True
                
            elif 'who is' in statement:
                person = statement.replace('who is','')
                info = wikipedia.summary(person, 5)
                boo2=True
                print(info)
                speak(info)

            elif "show me the weather" in statement:
                api_key="074d8b843fcd4636a3fdddeaf0a6300c"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
                city_name=takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                boo2 = True

            elif 'weather' in statement:
                speak("Where?")
                sitio = takeCommand().lower()
                webbrowser.open("https://www.eltiempo.es/"+sitio+".html",0,True)
                boo2 = True

            elif 'nothing' in statement:
                speak("Ok sir")
                boo = True
               
            elif 'shut down' in statement:
                print("Are you sure?")
                speak("Are you sure?")
                op = takeCommandJ().lower()
                boo2=True
                if 'yes' in op:
                    subprocess.call("shutdown -s")
                else:
                    speak("Ok sir")

            elif 'restart' in statement:
                speak("Restarting...")
                print("Restarting...")
                subprocess.call(["C:\\Users\\aleja\\Desktop\\Jarvis\\inicio.bat"])
                break

            if boo2:   
                boo2 = False
                speak("Something else?")
                no = takeCommandNO().lower()
                if "no" in no:
                    speak("Ok sir")
                    boo=True
                else:
                    boo=False
                    speak("Ok sir, tell me")

        else:
            continue
    time.sleep(2)