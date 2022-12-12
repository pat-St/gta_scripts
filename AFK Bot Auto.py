import time

import keyboard
import mouse
import pyautogui

global stop
stop = True


def warten():
    time.sleep(20)


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
        # keyboard.press('e')

        keyboard.press('w')
        if stop == True:
            break
        time.sleep(0.2)
        keyboard.release('w')

        if stop == True:
            break

        warten()
        print("a wird gedrückt")
        keyboard.press('a')
        if stop == True:
            break

        time.sleep(0.4)
        keyboard.release('a')
        if stop == True:
            break

        warten()
        print("d wird gedrückt")
        keyboard.press('d')
        if stop == True:
            break
        time.sleep(0.4)
        keyboard.release('d')
        if stop == True:
            break
        warten()
