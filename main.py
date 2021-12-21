import datetime
import math
import os
import random
import time
import webbrowser
from datetime import date
import re
import requests
import psutil
import pyautogui
import pyjokes
import PyPDF2
import pyttsx3
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from requests import get
from selenium import webdriver
from urllib.request import urlopen
import json
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        print(f"Good Morning sir. it has been {strTime}")
        speak(f"Good Morning sir. it has been {strTime}")
    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon sir. it has been {strTime}")
        speak(f"Good Afternoon sir. it has been {strTime}")
    else:
        print(f"Good Evening sir. it has been {strTime}")
        speak(f"Good Evening sir. it has been {strTime}")

def schedule_checker():
    today_day = date.today().strftime("%A")

    if today_day == "Monday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Tuesday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Wednesday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Thursday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Friday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Saturday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

    elif today_day == "Sunday":
        speak(f"It's {today_day}, Enjoy Your day sir!")

wish()
schedule_checker()

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    print("%s %s" % (s, size_name[i]))
    return "%s %s" % (s, size_name[i])

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening]...")
        audio = r.listen(source)
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source)  

    try:
        print("...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception:
        return "None"
    return query

def TaskExecution():
    while True:

        strTime = datetime.datetime.now().strftime("%I:%M %p")

        query = takecommand().lower()
        chrome_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        app = wolframalpha.Client('9U8EKY-LG937R6772')

        if "good morning" in query:
            speak("good morning sir")

        elif "good afternoon" in query:
            speak("good afternoon")

        elif "good evening" in query:
            speak("good evening")

        elif "good night" in query:
            speak("Good night sir, see you later.")

        elif "make new folder" in query or "create new folder" in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif "jump to desktop" in query:
            pyautogui.hotkey('win', 'd')
            speak("all tabs are minimized")

        elif "open vs code" in query:
            path = "C:\\Users\\pritg\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening Visual Studio Code')
            os.startfile(path)

        elif "close vs code" in query:
            speak('closing visual Studio Code')
            os.system("taskkill /f /im code.exe")

        elif "open discord" in query:
            path = "C:\\Users\\pritg\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
            speak("opening discord")
            os.startfile(path)

        elif "close discord" in query:
            speak('Closing discord')
            os.system("taskkill /f /im discord.exe")

        elif "open notepad" in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("Opening Notepad!")
            os.startfile(path)

        elif "close notepad" in query:
            speak("Closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "play music" in query or "hit some music" in query or "plays some music" in query:
            music_dir = "D:\\Music"
            speak("Sure Boss!")
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "open command prompt" in query:
            speak('opening command prompt')
            os.system("start cmd")

        elif "what is my ip" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
            print(f"Your ip address is {ip}")

        elif "who " in query or  query or "wikipedia " in query or "tell me about" in query or "give me information about" in query:
            try:
                query = query.replace("wikipedia", "")
                query = query.replace("according", "")
                query = query.replace("to", "")
                query = query.replace("friday", "")
                query = query.replace("tell me about", "")
                query = query.replace("give me information about", "")
                result = wikipedia.summary(query, sentences=5)
                speak('According to me')
                print(result)
                speak(result)
            except Exception:
                speak("No result Found...")

        elif "sleep the system" in query or "sleep system" in query:
            speak('System will be sleep in some seconds')
            os.system("rundll32.exe powrprof.dll, SetSuspendState  0,1,0")

        elif "restart the system" in query or "restart system" in query:
            speak('System will be restart in some seconds')
            os.system("shutdown /r /t 5")

        elif "shutdown the system" in query or "shutdown system" in query:
            speak('System will be shut in some seconds')
            os.system("shutdown /s /t 5")

        elif "switch the window" in query or "switch window" in query:
            speak('Sure Boss!')
            pyautogui.hotkey("alt", "tab")

        elif "search " in query:
            query = query.replace("search ", "")
            url = f"https://www.google.com/search?&q={query}"
            webbrowser.get("chrome").open_new_tab(url)
            speak('Sure Boss!')

        elif "joke" in query:
            s = pyjokes.get_joke(language='en', category='all')
            print(s)
            speak(s)
            print("Hahaha it was funny wasn't it?")
            speak("Hahaha it was funny wasn't it?")

        elif "hello" in query or "hey" in query or "hi" in query:
            text = random.choice(["Hello sir!", "Hey there!", "Hello..."])
            speak(text)

        elif "thanks" in query or "thanks friday" in query or "thank you friday" in query:
            thanks = random.choice(
                ["Your welcome sir", "no problem sir", "Anytime you want", "i am glad to here", "enjoy yourself, Sir"])
            speak(thanks)

        elif "how are you" in query:
            speak('I am always fine. what about you?')

        elif "fine" in query:
            speak("glad to here it. what's next command?")

        elif "what is your name" in query:
            speak("My name is friday.")

        elif "what can you do" in query:
            speak("I can do so many things such as calculating sums, doing computer tasks, some jokes and so many other things.")

        elif "who are you" in query:
            speak("I Am friday, I am your personal assistant, Made by my Boss, Preet")

        elif "i love you" in query:
            speak("It's hard to understand..")

        elif "marry me" in query or "marry with me" in query:
            speak("Uh..Oh.. It's better to become your assistant, Rather then something else...")

        elif "you are doing great" in query or "you great" in query:
            speak("Thanks Sir, Glad to listen it...")

        elif "help me" in query or "help" in query:
            speak("Ok Boss, Just tell me your query.")

        elif "who made you" in query or "who created you" in query or "who is your owner" in query or "who is your boss?" in query:
            speak("I was created by my Boss prit.")
        
        elif "system stats" in query or "check system" in query:
            def system_stats():
                cpu_stats = str(psutil.cpu_percent())
                # battery_percent = psutil.sensors_battery().percent
                memory_in_use = convert_size(psutil.virtual_memory().used)
                total_memory = convert_size(psutil.virtual_memory().total)
                final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used."
                return final_res

            sys_info = system_stats()
            print(sys_info)
            speak(sys_info)

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak("Sir, all the files in this folder are now hidden")

        elif "visible all files" in query or "make files visible" in query:
            os.system("attrib -h /s /d")
            speak(
                "Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

        elif "take a screenshot" in query or "take screenshot" in query:
            speak("sir, what should i name this screenshot?")
            name = takecommand()
            speak('Hold on i am taking screenshot..')
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Successfully taken screenshot and save in main folder.")

        elif "temperature" in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(f"The temperature outside is {next(res.results).text}")
            except Exception:
                speak("Boss, API Went wrong can't detect temperature.")

        elif "sleep" in query or "you need a break" in query:
            sleep_response = random.choice(["i am going to have  a cup of coffee, call me if you need anything",
                                            "Okay i am going to sleep then", "Good by sir have great day."])
            speak(sleep_response)
            break

        elif "volume up" in query or "increase volume" in query or "increase the volume" in query:
            pyautogui.press('volumeup')
            speak("Sure Boss!")

        elif "volume down" in query or "decrease volume" in query or "descrease the volume" in query:
            pyautogui.press('volumedown')
            speak("Sure Boss!")

        elif "volume mute" in query or "mute volume" in query or "mute the volume" in query or "mute" in query:
            pyautogui.press('volumemute')
            speak("Sure Boss!")

        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=697b84f285be437da7d510994deed38a''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "open website" in query:
            query = query.replace("dot", ".")
            query = query[12:]
            speak(f"opening {query}")
            print(f"{query}")
            url = f"{query}"
            webbrowser.get("chrome").open_new_tab(url)

        elif "new project in my private server" in query or "new private project" in query:
            speak(
                'Sir, Making a new project in your  private server.')
            pyautogui.hotkey('win', 'n')
            os.startfile("D:\\PRIVATE PROJECTS")
            time.sleep(2)
            speak("Sir, What should i index the project file?")
            fileName = takecommand().lower()
            pyautogui.hotkey('ctrl', 'shift', 'n')
            pyautogui.write(f"{fileName}")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            speak("Done, Boss")

        elif "new project in my public server" in query or "new public project" in query:
            speak(
                'Sir, Making a new project in your public server.')
            pyautogui.hotkey('win', 'n')
            os.startfile("D:\\PUBLIC PROJECTS")
            time.sleep(2)
            speak("Sir, What should i index the project file?")
            fileName = takecommand().lower()
            pyautogui.hotkey('ctrl', 'shift', 'n')
            pyautogui.write(f"{fileName}")
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            speak("Done, Boss")

        elif 'calculate' in query:
            question=query
            app_id="9U8EKY-LG937R6772 "
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(f"The answer is {answer}")
            print(f"The answer is {answer}")

        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")
            except Exception:
                speak("It's Already Empty.")
                
        elif "coordinates" in query:
            coordinates = pyautogui.position()
            speak(
                f"coordinates are {coordinates}, I also printed in terminal, You can check it.")
            print(
                f"coordinates are {coordinates}, I also printed in terminal, You can check it.")

        elif "what time" in query:
            print(f"It's {strTime}")
            speak(f"It's {strTime}")

        elif "what date" in query:
            today_date = date.today()
            print(f"It's {today_date}", )
            speak(f"It's {today_date}", )

        elif "what day" in query:
            today_day = date.today().strftime("%A")
            print(f"It's {today_day}", )
            speak(f"It's {today_day}", )
    
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('friday.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif 'launch' in query:
            query.replace("launch", "")
            query.replace(" ", "")
            pyautogui.hotkey("win", "s")
            time.sleep(1)
            # app=query[6:]
            pyautogui.write(app.lower())
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
            speak('I have launched the desired application')

        elif 'set reminder' in query:
            speak("What shall I remind you about?")
            text = takecommand()
            speak("In how many minutes?")
            local_time = int(takecommand())
            local_time = local_time * 60
            time.sleep(local_time)
            speak(f"it's a reminder for {text}")
            speak(f"it's a reminder for {text}")
            speak(f"it's a reminder for {text}")

if __name__ == "__main__":
    while True:

        permission = takecommand().lower()

        if "wake up" in permission or "hey friday" in permission or "are you here" in permission or "are you there" in permission or "friday you up" in permission or "you there" in permission or "you here" in permission or "friday you app" in permission or "i am back" in permission or "friday" in permission:
            wake_text = random.choice(
                ['Online and ready sir!', "At your service sir."])
            speak(wake_text)
            TaskExecution()