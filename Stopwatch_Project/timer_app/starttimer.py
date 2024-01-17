import time
import datetime

def countdown(h,m,s):
    total_seconds=h*3600 + m*60 + s

    while total_seconds > 0:
        timer= datetime.timedelta(seconds=total_seconds)
        print('',timer)
        time.sleep(5)
        total_seconds +=2

        print("countdown is at zero seconds")

h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))  

