import datetime
import os
import random
import time
import webbrowser
from datetime import date
import psutil
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
from requests import get
from urllib.request import urlopen
import json
import pywhatkit
import winsound
from pywikihow import WikiHow, search_wikihow
from src.functions.convert_size import convert_size
import phonenumbers
import folium
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier

import serial

ser = serial.Serial('COM15', 9600)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 194)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


winsound.PlaySound('D:\\Coding\\Public-Codes\\jarvis\\src\\files\\startup_checking.wav', winsound.SND_FILENAME)

hour = int(datetime.datetime.now().hour)
app = wolframalpha.Client('9U8EKY-LG937R6772')
fetch_temp = app.query("temperature")
temp = next(fetch_temp.results).text

if temp < str(20) and 0 <= hour < 18:
    weather = "Make sure to wear your jackets before yeeting outside! it's cold night!"
else:   
    weather = "Make sure to wear your jackets before yeeting outside!"

if temp > str(20) and hour > 18:
    weather = "It's Beautiful night outside!"
else:
    weather = "It's bright sunny day outside!"

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("[Listening]...")
        audio = r.listen(source, phrase_time_limit=2)
        r.pause_threshold = 0.5
    try:
        query = r.recognize_google(audio, language='en-us')
        print("...")
        print(f"You Said: {query}\n")

    except Exception:
        return "None"
    return query


def GoogleSearch(term):
    query = term.replace('jarvis', "")
    # query = query.replace("what is", "")
    query = query.replace("friday", "")
    query = query.replace("search", "")
    query = query.replace("google", "")
    # query = query.replace("how to ", "")
    # query = query.replace("who is", "")
    query = query.replace("according to you", "")
    writeab = str(query)

    Query = str(term)
    # os.startfile("D:\\Coding\\Public-Codes\\Jarvis\\database\\ExtraPro\\start.py")
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_result=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(Query, 3)
        speak(f"According to me, {search}")


def wish():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    today_day = date.today().strftime("%A")

    if 0 <= hour < 12:
        print(f"Good Morning, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")
        speak(f"Good Morning, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")
    elif 12 <= hour < 18:
        print(f"Good Afternoon, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")
        speak(f"Good Afternoon, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")
    else:
        print(f"Good Evening, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")
        speak(f"Good Evening, it has been {strTime}. It's {today_day}, The temperature outside is {temp}, {weather}")


def TaskExecution():
    while True:

        strTime = datetime.datetime.now().strftime("%I:%M %p")

        query = takecommand().lower()

        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        app = wolframalpha.Client('9U8EKY-LG937R6772')

        if "good morning" in query:
            speak("good morning")

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

        elif "play music" in query or "hit some music" in query or "plays some music" in query:
            music_dir = "D:\\Music"
            speak("Sure Boss!")
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "open command prompt" in query or "open cmd" in query:
            speak('opening command prompt')
            os.system("start cmd")

        elif "what is my ip" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")
            print(f"Your ip address is {ip}")

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

        elif "joke" in query:
            s = pyjokes.get_joke(language='en', category='all')
            print(s)
            speak(s)
            print("Haha, it was funny wasn't it?")
            speak("Haha, it was funny wasn't it?")

        elif "thanks" in query or "thanks jarvis" in query or "thank you jarvis" in query or "thank you" in query:
            thanks = random.choice(
                ["Your welcome sir", "no problem sir", "Anytime you want", "i am glad to here", "enjoy yourself, Sir"])
            speak(thanks)

        elif "how are you" in query:
            speak('I am always fine. what about you?')

        elif "fine" in query:
            speak("glad to here it. Let me know if you need any help!")

        elif "what is your name" in query:
            speak("My name is jarvis.")

        elif "what can you do" in query:
            speak(
                "I can do so many things such as calculating sums, doing computer tasks, some jokes and so many other "
                "things.")

        elif "who are you" in query:
            speak("I Am jarvis, I am personal assistant, Made by my Boss, Preet")

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
                final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used. "
                return final_res

            sys_info = system_stats()
            print(sys_info)
            speak(sys_info)

        elif "take a screenshot" in query or "take screenshot" in query:
            name = query.split("index it ", 1)
            img = pywhatkit.take_screenshot(f"{name[1]}")
            speak("Successfully taken screenshot and save in main folder.")

        elif "sleep" in query or "you need a break" in query:
            sleep_response = random.choice(["Okay i am going to sleep then", "Good by sir have great day."])
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
                jsonObj = urlopen(
                    '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey
                    =697b84f285be437da7d510994deed38a''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')
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

        elif "create new project" in query or "create a new project" in query:
            speak("should i create it in public or private database?")
            pub_pri = takecommand().lower()
            if "private" in pub_pri:
                speak("working on a secret project sir!")
                pyautogui.hotkey('win', 'm')
                os.startfile("D:\\coding\\Personal-Codes")
                time.sleep(2)
                fileName = query.split("index it as", 1)
                pyautogui.hotkey('ctrl', 'shift', 'n')
                try:
                    pyautogui.write(f"{fileName[1]}")
                except Exception as e:
                    speak("I wasn't able to name the project file!")
                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')
                speak("Done, Boss")
            elif "public" in pub_pri:
                speak(
                    'Sir, Making a new project in your public server.')
                pyautogui.hotkey('win', 'm')
                os.startfile("D:\\coding\\Public-Codes")
                time.sleep(2)
                fileName = query.split("index it as", 1)
                pyautogui.hotkey('ctrl', 'shift', 'n')
                try:
                    pyautogui.write(f"{fileName}")
                except Exception as e:
                    speak("I wasn't able to name the project file!")
                pyautogui.keyDown('enter')
                pyautogui.keyUp('enter')
                speak("Done, Boss")

        elif 'calculate' in query:
            question = query
            app_id = "9U8EKY-LG937R6772"
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
            file = open('jarvis.txt', 'w')
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
            query = query.replace("launch", "")
            query = query.replace("jarvis", "")
            pyautogui.hotkey("win", "s")
            time.sleep(1)
            # app=query[6:]
            pyautogui.write(query)
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
            speak('I have launched the desired software')

        elif "minimize" in query or "minimise" in query:
            speak("sure!")
            pyautogui.hotkey("win", "down")
            pyautogui.hotkey("win", "down")

        elif "open my online class time table" in query:
            path = "E:\\COLLEGE 2021\\PDFs\\Online-Class-TimeTable.pdf"
            speak("Sure, Boss!")
            os.startfile(path)

        elif "temperature" in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except Exception as e:
                print(e)
                speak("Something went wrong!")

        elif "play" in query or "song" in query:
            query = query.replace("play", " ")
            query = query.replace("jarvis", " ")
            query = query.replace("jarvis", " ")
            query = query.replace("song", " ")
            pywhatkit.playonyt(query)
            speak("sure!")

        elif "close the app" in query:
            speak("Sure!")
            pyautogui.hotkey('alt', 'f4')

        elif "search" in query:
            query = query.replace("jarvis", "")
            # query = query.replace("what is", "")
            query = query.replace("friday", "")
            query = query.replace("search", "")
            query = query.replace("google", "")
            # query = query.replace("how to ", "")
            # query = query.replace("who is", "")
            query = query.replace("according to you", "")
            GoogleSearch(query)

        elif "schedule shutdown" in query:
            speak("Tell me the seconds to shutdown the computer after that!")
            sec = takecommand().lower()
            sec = sec.replace("seconds", "")
            sec = int(sec)
            speak(f"System shutdown initiated in {sec} seconds")
            shutdown = f"shutdown /s /t {sec}"
            time.sleep(sec)
            os.system(shutdown)

        elif "track number" in query or "track phone number" in query or "track a phone number" in query:
            number = query.split("number", 1)
            number = number.replace("one", "1")
            number = number.replace("two", "2")
            number = number.replace("three", "3")
            number = number.replace("four", "4")
            number = number.replace("five", "5")
            number = number.replace("six", "6")
            number = number.replace("seven", "7")
            number = number.replace("eight", "8")
            number = number.replace("nine", "9")
            number = number.replace("zero", "0")
            number = number.replace("plus", "+")


            Key = "2b7bb8be109842db9431dcfa0ea8eecd"
            try:
                speak("Tracking Asked Number...")
                samNumber = phonenumbers.parse(number[1])
                yourLocation = geocoder.description_for_number(samNumber, "en")
                print(yourLocation)
                speak(f"Device with this number is in {yourLocation} right now!")
                service_provider = phonenumbers.parse(number[1])
                sim_provider = carrier.name_for_number(service_provider, "en")
                speak(f"sim service provider {sim_provider}")
                geocoder = OpenCageGeocode(Key)
                query = str(yourLocation)
                results = geocoder.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                speak("Latitude and Longitude Found!")
                print(lat, lng)
                myMap = folium.Map(location=[lat, lng], zoom_start=9)
                folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))
                speak("Saving Location File!")
                myMap.save("myLocation.html")
                speak("Opening location in Google Maps")
                os.startfile("Location.html")
            except Exception as e:
                print(e)
                speak("Number not found!")

        elif "google" in query:
            query = query.replace("google", "")
            query = query.replace("search", "")
            query = query.replace("jarvis", "")
            webbrowser.get('chrome').open(query)

        # Arduino Automation!   

        elif "turn on the lamp" in query or "turn the lamp on" in query or "turn on lamp" in query in "lamp on" in query or "turn on the lamp" in query:
            ser.write(b'1 bulb on')
            speak("lamp on!")
            print("lamp on!")

        elif "turn off the lamp" in query or "turn the lamp off" in query or "turn off lamp" in query or "lamp off" in query or "turn off the lamp" in query:
            ser.write(b'1 bulb off')
            speak("lamp off!")
            print("lamp off!")


if __name__ == "__main__":
    wish()
    while True:
        permission = takecommand().lower()
        if "jarvis" in permission or "wake up" in permission:
            winsound.PlaySound('D:\\Coding\\Public-Codes\\jarvis\\src\\files\\start_up_sound.mp3',
                               winsound.SND_FILENAME)
            TaskExecution()
