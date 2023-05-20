import threading
from playsound import playsound


def inita():
    playsound('Jarvis Startup.mp3')
x = threading.Thread(target=inita)
x.start()


import pyttsx3
import time
import wikipedia
import speech_recognition as sr
import datetime
import os
from AppOpener import  run
import random
import webbrowser
import text2emotion
import pandas as pd

time.sleep(17)

# from greeting import greet

# Init
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# 2. time hour
time = datetime.datetime.now().hour

# 3. Synonyms
a_ = ["What you want to do today?", "How may I help you?", "Do i have anything to assist you?", "Is there any way for me to assist you?"  ]
thank_ = ["thanks", "thank", "appretiated", "appretiate", "you are best", "you are the best", "owe you", "welcomed"]

query = None

data_feel = pd.read_csv("feel.csv")
# happy, afraid,sad,depressed,angry,surprised,exited,hurt
happy_list = data_feel["happy"].tolist()
afraid_list = data_feel["afraid"].tolist()
sad_list = data_feel["sad"].tolist()
depressed_list = data_feel["depressed"].tolist()
angry_list = data_feel["angry"].tolist()
surprise_list = data_feel["surprised"].tolist()
exited_list = data_feel["exited"].tolist()
hurt_list = data_feel["hurt"].tolist()


def speak(speech):
    print("Alex: ", speech)
    engine.say(speech)
    engine.runAndWait()

def speakWithoutSubs(speech):    
    engine.say(speech)
    engine.runAndWait()


def audio_init():
    global query
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
        query = "Test"

    try:
        print("Recognizing...")
        query = recognizer.recognize_bing(audio, language='en-IN')
        str(query)
        print(f"You: {query}\n")
        return query

    except Exception as e:
        print(e)
        audio_init()

def greeting(): 
    if time >= 0 and time <= 12:
        speak("Good Morning Sir")
    elif time > 12 and time <= 4:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir")
    speak("How are you doing sir!")
    
    speak(random.choice(a_))


def sturc(query):
        if "coding" in query or "code" in query or "open code" in query:
                    playsound('process.mp3')
                    run("Visual Studio Code")
        elif "open" in query:
            playsound("process.mp3")
            a = query
            a = list(a.split(" "))
            ind = a.index('open')
            try:
                try:
                    run(str(a[ind+1]))
                except Exception as e: 
                    try:
                        webbrowser.open(str(a[ind+1]) + ".com", 2)
                    except Exception as e:
                        try:
                            run(str(a[ind+1])+" "+str(a[ind+2]))
                        except Exception as e:
                            run(str(a[ind+1])+" "+str(a[ind+2]) + " "+str(a[ind+3]))
            except Exception as e:
                playsound("else.mp3")
                speak("I am sorry sir! I have encountered with a error")
                
        elif 'search' in query:
            playsound("process.mp3")
            a = list(a.split(" "))
            temp = a.index('search')
            search = str(a[temp+1:])
            temp = wikipedia.summary(search, sentences = 2)
            print(temp)
        
        elif 'open stack overflow' in query:
            try:
                webbrowser.open("stackoverflow.com")
                speak("Opening stackoverflow")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open white hat' in query:
            try:
                webbrowser.open("https://code.whitehatjr.com/s/dashboard")
                speak("Opening whitehat jr")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, I am not able to do this task!")

        
        
        else:
            try:
                playsound("process.mp3")
                temp = wikipedia.summary(query, sentences = 2)
                speak(temp)
            except Exception as Err:
                playsound("else.mp3")
                speak("I am sorry sir! I have encountered with a error")


    
    
# Alex.speak("The time is: " + time + "hours")







if __name__ == "__main__":
    greeting()
    
    
    while True:
        audio_init()
        happy = ["Its good to listen you happy", "Its a pleasure to listen you happy", "Be happy with what you have. Be excited about what you want.", "You have a great sense of humor.", "If cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now."]
        sad = ['Its OK to not feel OK', 'You are not alone', "I'm here for you, no matter what", "Your story isn't over"]
    
        emotion = text2emotion.get_emotion(query)
        if emotion:
            
            try:
                emot = max(zip(emotion.values(), emotion.keys()))[1]
                if emot == 'Angry' or emot == 'Fear':
                    temp_list = afraid_list+ angry_list
                    phrase = random.choice(temp_list)
                    speak(phrase)
                    sturc(query)
                elif emot == 'Happy':
                    temp_list = happy_list + surprise_list + exited_list + happy
                    phrase = random.choice(temp_list)
                    speak(phrase)
                    sturc(query)
                elif emot == 'Sad':
                    temp_list = sad_list+ depressed_list + sad + hurt_list
                    speak(random.choice(temp_list))
                    sturc(query)
                else:
                    sturc(query)

            except Exception as e:
                continue