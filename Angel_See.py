import time

import keyboard
import mouse
import numpy as np
from PIL import ImageGrab

from fishing import FishSymbolDetection

# import pyautogui


global stop
stop = True


def isWeiss(game_coords):
    screenshot = ImageGrab.grab(
        bbox=game_coords, include_layered_windows=True, all_screens=True)
    erkennung = np.array(screenshot)
    print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])

    print("x:" + str(xlen) + " y:" + str(ylen))
    midX = xlen // 2
    midY = ylen // 2

    print("mitte: x:" + str(midX) + " y:" + str(midY))

    r = erkennung[midX, midY][0]
    g = erkennung[midX, midY][1]
    b = erkennung[midX, midY][2]
    if [27, 97, 143] == [r, g, b]:
        print("Fisch einziehen ")
        keyboard.release('a')
        keyboard.release('d')
        mouse.press('left')
        time.sleep(17)
        mouse.release('left')
        time.sleep(4)
        keyboard.press_and_release('e')
        return True
    return False


def start_event():
    global stop
    stop = False
    print("Start")


def stop_event():
    global stop
    stop = True
    print("Wird Pausiert")


keyboard.add_hotkey('x', lambda: start_event())
keyboard.add_hotkey('p', lambda: stop_event())

fishDetection = FishSymbolDetection(
    model_path=".\\assets\\model2.pt", showOutput=False)
# model_path=".\\model.pt", showOutput=False)
# fishDetection = FishSymbolDetection(model_path="assets\model.pt")xp
# fishDetection.useScreenshotInput([0, 20, 650, 700])
# fishDetection.useVideoInput(".\\assets\\fischen_dark.mp4")
fishDetection.useVideoInput(0)
while True:
    # warten bis eingabe dann start
    print("Zum Starten x drücken p zum Pausieren")
    while stop == True:
        time.sleep(2)

    fishDetection.start()
    while stop == False:
        # keyboard.press_and_release('e')
        start = None
        now = None
        fishsymbol = fishDetection.detectFish()
        if fishsymbol.detected():
            start = time.time()
            if fishsymbol.isLeft():
                print("fish directed to left")
                print("D wird gehalten")
                keyboard.release('a')
                keyboard.press('d')
            if fishsymbol.isRight():
                print("fish directed to right")
                print("A wird gehalten")
                keyboard.release('d')
                keyboard.press('a')
        else:
            now = time.time()
            if start and now - start < 1:
                start = None
                now = None
                keyboard.release('a')
                keyboard.release('d')
                print("Taste wird losgelassen")

        print("Warte bis nächste runde")
        time.sleep(2)
        if isWeiss([1867, 1000, 1890, 1010]):
            time.sleep(1)
    print("Taste wird losgelassen")
    keyboard.release('a')
    keyboard.release('d')

    print("Fischerkennung beendet")
    fishDetection.stop()
