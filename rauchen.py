import time

import keyboard
import mouse
import pyautogui

global stop
stop = True


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
    print("Was verwendet wird auf Slot 2 setzen")
    while stop == True:
        time.sleep(1)

    while stop == False:

        keyboard.press('2')
        time.sleep(0.4)
        keyboard.release('2')
        time.sleep(1)
