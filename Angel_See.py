import time

import keyboard
import mouse
import pyautogui

from fishing import FishSymbolDetection

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

fishDetection = FishSymbolDetection()
fishDetection.useScreenshotInput([100, 500, 2200, 1900])
while True:
    # warten bis eingabe dann start
    print("Zum Starten x drücken d und e zum Pausieren")
    while stop == True:
        time.sleep(2)

    fishDetection.start()
    while stop == False:
        fishsymbol = fishDetection.detectFish()
        if fishsymbol.detected():
            if fishsymbol.isLeft():
                print("fish directed to left")
                print("A wird gehalten")
                pyautogui.keyDown('a')
                pyautogui.keyUp('d', _pause=False)
            if fishsymbol.isRight():
                print("fish directed to right")
                print("D wird gehalten")
                pyautogui.keyDown('d')
                pyautogui.keyUp('a', _pause=False)
        else:
            print("Taste wird losgelassen")
            pyautogui.keyUp('a', _pause=False)
            pyautogui.keyUp('d', _pause=False)
        print("Warte bis nächste runde")
        # time.sleep(7)
    print("Taste wird losgelassen")
    pyautogui.keyUp('a', _pause=False)
    pyautogui.keyUp('d', _pause=False)
    fishDetection.stop()
