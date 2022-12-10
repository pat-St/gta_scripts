import mouse
import keyboard
import time
import pyautogui


global stop
stop = True

def warten():
   time.sleep (10)

def start_event():
    global stop
    stop = False
    print("Start")

def stop_event():
    global stop
    stop = True
    print("Wird Pausiert")

keyboard.add_hotkey('x', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

while True:

    # warten bis eingabe dann start
    print("Das was du im Inventar benutzen willst lege es auf schnellzugriff 2")
    print("Zum Starten x drücken dund e zum Pausieren")
    while stop == True:
        time.sleep(2)

    
        
    while stop == False:
        keyboard.press('2')
        time.sleep(0.2)
        keyboard.release('2')
        warten()