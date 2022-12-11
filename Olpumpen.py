import time

import keyboard
import mouse
import numpy as np
from PIL import ImageGrab

#game_coords = [653, 347, 1142, 763]


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
    if [250, 250, 250] == [r, g, b]:
        print("is weiß")
        return True
    return False


def Anfang():
    sx = 10
    sy = 10
    x1 = 810
    x2 = x1+sx
    y1 = 510
    y2 = y1+sy
    ersterBlock = [x1, y1, x2, y2]
    gelb = [250, 200, 2]
    print("Start")


def drücken():
    mouse.press('left')
    time.sleep(3.8)
    mouse.release('left')


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


keyboard.add_hotkey('q', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

while True:

    # warten bis eingabe dann start
    print("Zum Starten q drücken und e zum Pausieren")
    while stop == True:
        time.sleep(1)

    while stop == False:
        mouse.move(300, 600, absolute=True)
        drücken()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(400, 600, absolute=True)
        drücken()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(500, 600, absolute=True)
        drücken()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(500, 600, absolute=True)
        drücken()

        if isWeiss([653, 347, 1142, 763]):
            stop = True
