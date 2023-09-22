import time

import keyboard
import mouse
import pyautogui

global stop
stop = True


def warten():
    print("5 Sekunden Pause")
    time.sleep(5)

def PressA():
    keyboard.press('a')
    time.sleep(0.4)
    keyboard.release('a')
    print("A wird gedrückt")

def PressD():
    keyboard.press('d')
    time.sleep(0.4)
    keyboard.release('d')
    print("D wird gedrückt")

def PressW():
    keyboard.press('w')
    time.sleep(0.4)
    keyboard.release('w')   
    print("W wird gedrückt") 


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
    print("Zum Starten x drücken dund e zum Pausieren")
    while stop == True:
        time.sleep(1)

    while stop == False:
        warten()

        PressA()

        warten()

        if stop == True:
            break

        PressD()

        warten()

        PressW()
        
        if stop == True:
            break

