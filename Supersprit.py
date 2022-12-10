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


def warten():
    time.sleep(0.3)


keyboard.add_hotkey('x', lambda: start_event())
keyboard.add_hotkey('e', lambda: stop_event())

while True:

    # warten bis eingabe dann start
    print("Zum Starten x drücken dund e zum Pausieren")
    while stop == True:
        warten()

    while stop == False:
        # ins inventar gehen
        keyboard.press('i')
        warten()
        keyboard.release('i')
        if stop == True:
           break

        # Gegenstand herstellen drückern
        x = 1618
        y = 30
        warten()
        mouse.move(x, y, absolute=True)
        mouse.click('left')
        warten()
        if stop == True:
           break

        # auf Kategorie drücken
        x2 = 665
        y2 = 143
        warten()
        mouse.move(x2, y2, absolute=True)
        mouse.click('left')
        warten()
        if stop == True:
           break

        # ins drop down menu
        x5 = 666
        y5 = 346
        mouse.move(x5, y5, absolute=True)
        warten()
        if stop == True:
           break

        # runterscrollen

        pyautogui.scroll(-50000)
        warten()

        # auf andere drücken
        x3 = 598
        y3 = 471
        mouse.move(x3, y3, absolute=True)
        mouse.click('left')
        warten()
        if stop == True:
           break

        # auf premium kanister drücken
        x4 = 401
        y4 = 413
        warten()
        mouse.move(x4, y4, absolute=True)
        mouse.click('left')
        if stop == True:
           break

        warten()

        # item herstellen drücken
        x6 = 1384
        y6 = 780
        warten()
        mouse.move(x6, y6, absolute=True)
        mouse.click('left')
        if stop == True:
           break
