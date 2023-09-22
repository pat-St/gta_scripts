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
    print("Zum Starten x drücken d und e zum Pausieren")
    while stop == True:
        time.sleep(2)

    while stop == False:

        print("E wird gehalten")

        pyautogui.keyDown('e')

        if stop == True:
            print("wait")

        time.sleep(5)

        print("Taste wird losgelassen")

        pyautogui.keyUp('e', _pause=False)

        print("Warte bis nächste runde")
        
        time.sleep(7)
