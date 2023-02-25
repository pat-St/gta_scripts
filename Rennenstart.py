import time

import keyboard
import mouse
import pyautogui

global stop
stop = True

def warten():
   time.sleep (0.21)

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
        time.sleep(1)

    
        
    while stop == False:
        pyautogui.press("g")
        warten()
        pyautogui.press("7")
        warten()
        x = 940
        y = 519
        mouse.move(x, y, absolute=True)
        warten()
        mouse.click("left")
        #mouse.release('left')
        warten()

        if stop == True:
            break

        x = 865
        y = 650
        mouse.move(x, y, absolute=True)
        warten()
        mouse.click("left")
        #mouse.release('left')
        warten()
        if stop == True:
            break

        x = 913
        y = 596
        mouse.move(x, y, absolute=True)
        warten()
        mouse.click("left")
        #mouse.release('left')
        warten()
        if stop == True:
            break

        pyautogui.typewrite("1")
        warten()

        x = 859
        y = 731
        mouse.move(x, y, absolute=True)
        warten()
        mouse.click("left")
        warten()
        #mouse.release('left')

        if stop == True:
            break


        keyboard.press('esc')
        print("esc wird gedrückt")
        if stop == True:
             break
        time.sleep(0.1)
        keyboard.release('esc')
        if stop == True:
             break
        warten()
        keyboard.press('enter')
        if stop == True:
             break
        warten()
        keyboard.release('enter')
        if stop == True:
             break

        warten()

        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)
        pyautogui.scroll(50000)

        warten()

        keyboard.press('w')
        time.sleep(0.042)
        keyboard.release('w')
        warten()

        keyboard.press('enter')
        time.sleep(0.01)
        keyboard.release('enter')
        keyboard.press('esc')
        time.sleep(0.1)
        keyboard.release('esc')
        time.sleep(0.1)

        keyboard.press('esc')
        time.sleep(0.1)
        keyboard.release('esc')
        time.sleep(0.1)
        time.sleep(1)
        # keyboard.press('esc')
        # time.sleep(0.1)
        # keyboard.release('esc')

        
    







