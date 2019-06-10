#!/usr/bin/python3
import time
name=input("Please Enter Your Name: \n")
currtime=int(time.strftime("%H"))
if currtime>5 and currtime<11:
    print("Good Morning "+name)
elif currtime>=11 and currtime<16:
    print("Good Afternoon "+name)
elif currtime>=16 and currtime<21:
    print("Good Evening "+name)
else:
    print("Good Night "+name)
