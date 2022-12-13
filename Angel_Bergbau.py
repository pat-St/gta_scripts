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
    while stop == True:
        time.sleep(2)

    while stop == False:

        # mouse.click('left')
        print("E wird gehalten")
       # time.sleep(6)
        pyautogui.keyDown('e')
        time.sleep(5)
        print("Taste wird losgelassen")
        pyautogui.keyUp('e', _pause=False)

        print("Warte bis nächste runde")
        time.sleep(7)
