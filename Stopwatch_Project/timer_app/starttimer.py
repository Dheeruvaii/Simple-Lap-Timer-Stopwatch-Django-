import time
import datetime
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()
def countdown(h,m,s):
    total_seconds=h*3600 + m*60 + s

    while total_seconds > 0:
        timer= datetime.timedelta(seconds=total_seconds)
        speak(str(timer))
        print('',timer)
        time.sleep(5)
        total_seconds -=2

        speak("countdown is at zero seconds")
        print("countdown is at zero seconds")

h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))  

