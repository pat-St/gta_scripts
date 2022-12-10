import mouse
import keyboard
import time
import pyautogui


global stop
stop = True

def warten():
   time.sleep (0.8)

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
        keyboard.press('i')
        keyboard.release('i')
        warten()

        if stop == True:
            break

        # geganstand herstellen
        x = 1665
        y = 36
        mouse.move(x, y, absolute=True)
        mouse.click('left')
        warten()

        if stop == True:
            break

        #kategorien

        x2 = 728
        y2 = 144
        mouse.move(x2, y2, absolute=True)
        mouse.click('left')
        warten()

        if stop == True:
            break

        #drop down menu

        x3 = 633
        y3 = 463
        mouse.move(x3, y3, absolute=True)

        warten()

        if stop == True:
            break

        #drop down menu scropllen u auf andere klicken

        pyautogui.scroll(-50000)

        x4 = 633
        y4 = 463
        mouse.move(x4, y4, absolute=True)
        mouse.click('left')
        warten()

        if stop == True:
            break

        #auf premium kanister drücken

        x5 = 378
        y5 = 395
        mouse.move(x5, y5, absolute=True)
        mouse.click('left')
        warten()
        
        if stop == True:
            break
        #premiumkanister herstellen

        x6 = 1388
        y6 = 776
        mouse.move(x6, y6, absolute=True)
        mouse.click('left')



