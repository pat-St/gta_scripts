import time
import sys
import keyboard
import mouse
import numpy as np
from PIL import ImageGrab

#game_coords = [653, 347, 1142, 763]


def isWeiss(game_coords):
    screenshot = ImageGrab.grab(
        bbox=game_coords, include_layered_windows=True, all_screens=True)
    erkennung = np.array(screenshot)
    # print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])

    # print("x:" + str(xlen) + " y:" + str(ylen))
    midX = xlen // 2
    midY = ylen // 2

    # print("mitte: x:" + str(midX) + " y:" + str(midY))

    r = erkennung[midX, midY][0]
    g = erkennung[midX, midY][1]
    b = erkennung[midX, midY][2]
    if [250, 250, 250] == [r, g, b]:
        print("is weiß")
        return True
    print("r:", r,"g:",g,"b:",b)
    return False
    

IS_BOOST = False

selection = input("Boost? (y|N)")

if (len(selection) > 0) and (str(selection).lower() == 'y'):
    IS_BOOST = True
    print("Boost Aktiviert")
else:
    IS_BOOST = False
    print("Boost Deaktiviert")



def drücken():
        mouse.press('left')
        time.sleep(3.8)
        mouse.release('left')
        print("Taste wird gehalten")

def drückenboost():
        mouse.press('left')
        time.sleep(2.5)
        mouse.release('left')
        print("Taste wird gehalten")


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
        mouse.move(2218, 600, absolute=True)
        
        if IS_BOOST:
            drückenboost()
        else:
            drücken()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(2323, 600, absolute=True)
        if IS_BOOST == False:
            drücken()
        else:
            drückenboost()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(2428, 600, absolute=True)
        if IS_BOOST == False:
            drücken()
        else:
            drückenboost()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

        while stop == True:
            time.sleep(1)
            print("Warte")

        mouse.move(2532, 600, absolute=True)
        if IS_BOOST == False:
            drücken()
        else:
            drückenboost()

        if isWeiss([653, 347, 1142, 763]):
            stop = True

    