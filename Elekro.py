import time

import keyboard
import mouse
import numpy as np
import pyautogui
from PIL import ImageGrab

# Geschwindigkeit
duration = 0.5


def warten():
    time.sleep(0.1)


def hatFarbe(screenshot_fenster, farbe):
    screenshot = ImageGrab.grab(
        bbox=screenshot_fenster, include_layered_windows=True, all_screens=True)
    erkennung = np.array(screenshot)
    xlen = len(erkennung)
    ylen = len(erkennung[0])

    midX = xlen // 2
    midY = ylen // 2

    r = erkennung[midX, midY][0]
    g = erkennung[midX, midY][1]
    b = erkennung[midX, midY][2]

    fr = farbe[0]
    fg = farbe[1]
    fb = farbe[2]

    if fr <= r and fg <= g and fb <= b:
        # print("‐●                                     ●‐")
        # print("‐● Eine Leitung wurde erfolgeich gelöst ●‐")
        # print("‐●                                     ●‐")
        return True
    return False


# Test auf Gelöste Schalttafel
def wurdeGeloest():
    erfolgGruen = [0, 100, 0]
    return hatFarbe([1860, 20, 1900, 70], farbe=erfolgGruen)


def alleBloeckeSindVerbunden():
    warten()
    return not (hatErsterBlock() and hatZweiterBlock() and hatDritterBlock())


def hatErsterBlock():
    sx = 10
    sy = 10
    x1 = 1005
    x2 = x1+sx
    y1 = 591
    y2 = y1+sy
    ersterBlock = [x1, y1, x2, y2]
    gelb = [250, 200, 2]
    # print("Erster block")
    return hatFarbe(ersterBlock, gelb)


def hatZweiterBlock():
    sx = 10
    sy = 10
    x1 = 1053
    x2 = x1+sx
    y1 = 580
    y2 = y1+sy
    zweiterBlock = [x1, y1, x2, y2]
    orange = [200, 100, 20]
    # print("Zweiter block")
    return hatFarbe(zweiterBlock, orange)


def hatDritterBlock():
    sx = 10
    sy = 10
    x1 = 1091
    x2 = x1+sx
    y1 = 580
    y2 = y1+sy
    dritterBlock = [x1, y1, x2, y2]
    gruen = [0, 160, 70]
    # print("Dritter block")
    return hatFarbe(dritterBlock, gruen)

# Visueller start trigger
# screenshot_fenster=[x1,y1,x2,y2]


def schalttafelErkannt(screenshot_fenster):
    screenshot = ImageGrab.grab(
        bbox=screenshot_fenster, include_layered_windows=True, all_screens=True)
    erkennung = np.array(screenshot)
    xlen = len(erkennung)
    ylen = len(erkennung[0])
    midX = xlen // 2
    midY = ylen // 2

    r = erkennung[midX, midY][0]
    g = erkennung[midX, midY][1]
    b = erkennung[midX, midY][2]
    if [51, 87, 105] == [r, g, b]:
        print("‐● Schalttafel wurde erkannt ●‐")
        return True
    return False


# User start/stop tasteneingabe
def start_event():
    global stop
    stop = False
    print("Start")


def stop_event():
    global stop
    stop = True
    print("Wird Pausiert")


def durchlauf1():
    global stop
    print("‐● Löse mit 1. Durchlauf ●‐")
    if hatErsterBlock():
        pyautogui.moveTo(1011, 586)
        pyautogui.dragTo(872, 594, button='left',
                         duration=duration)  # Gelb / Blau
        pyautogui .mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return  # raus anstatt weiter

    if hatZweiterBlock():
        pyautogui.moveTo(1053, 591)
        pyautogui.dragTo(874, 537, button='left',
                         duration=duration)  # Orange / Pink
        pyautogui.mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return

    if hatDritterBlock():
        pyautogui.moveTo(1093, 592)
        pyautogui.dragTo(1055, 533, button='left',
                         duration=duration)  # Grün / Braun
        pyautogui.mouseUp(button='left')


def durchlauf2():
    global stop
    print("‐● Löse mit 2. Durchlauf ●‐")
    if hatErsterBlock():
        pyautogui.moveTo(1011, 586)
        pyautogui.dragTo(874, 537, button='left', duration=duration)
        pyautogui.mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return  # raus anstatt weiter

    if hatZweiterBlock():
        pyautogui.moveTo(1053, 591)
        pyautogui.dragTo(1055, 533, button='left',
                         duration=duration)  # Orange / Braun
        pyautogui.mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return

    if hatDritterBlock():
        pyautogui.moveTo(1093, 592)
        pyautogui.dragTo(872, 597, button='left',
                         duration=duration)  # Grün / Blau
        pyautogui.mouseUp(button='left')


def durchlauf3():
    global stop
    print("‐● Löse mit 3. Durchlauf ●‐")
    if hatErsterBlock():
        pyautogui.moveTo(1011, 586)
        pyautogui.dragTo(1055, 533, button='left',
                         duration=duration)  # Gelb / Braun
        pyautogui.mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return  # raus anstatt weiter

    if hatZweiterBlock():
        pyautogui.moveTo(1053, 591)
        pyautogui.dragTo(872, 597, button='left',
                         duration=duration)  # Orange / Blau
        pyautogui.mouseUp(button='left')

    if wurdeGeloest() or stop == True:
        return

    if hatDritterBlock():
        pyautogui.moveTo(1093, 592)
        pyautogui.dragTo(874, 537, button='left',
                         duration=duration)  # Grün / Pink
        pyautogui.mouseUp(button='left')


global stop
stop = True

keyboard.add_hotkey('q', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

duration = 0.5
counterLoop = 0

while True:
    if stop == True:
        print("‐●                       ●‐")
        print("‐● Warte auf Schalttafel ●‐")
        print("‐●                       ●‐")

    # warten bis eingabe
    while stop == True:
        time.sleep(0.5)
        if schalttafelErkannt([780, 347, 1142, 763]):
            # fange an zu lösen
            stop = False

    # loop bis gelöst wurde
    while stop == False:
        if alleBloeckeSindVerbunden():
            # wurde gelöst
            stop = True
            break

        durchlauf1()

        if wurdeGeloest() or stop == True:
            break

        durchlauf2()

        if wurdeGeloest() or stop == True:
            break

        durchlauf3()

        if wurdeGeloest() or stop == True:
            break
