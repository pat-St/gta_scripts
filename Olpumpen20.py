import mouse
import keyboard
import time
from PIL import ImageGrab
import numpy as np

#game_coords = [653, 347, 1142, 763]

def isWeiss(game_coords):
    screenshot = ImageGrab.grab(bbox=game_coords,include_layered_windows=True,all_screens=True)
    erkennung = np.array(screenshot)
    print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])

    print("x:" + str(xlen) + " y:" + str(ylen))
    midX = xlen //2
    midY = ylen //2

    print("mitte: x:" + str(midX) + " y:" + str(midY))

    r = erkennung[midX,midY][0]
    g = erkennung[midX,midY][1]
    b = erkennung[midX,midY][2]
    if [250, 250, 250] == [r,g,b]:
        print("is weiß")
        return True
    return False


# def wurdeGeloest():
#     erfolgGruen = [0, 100, 0]
#     return hatFarbe([1860, 20, 1900, 70], farbe=erfolgGruen)

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
    

global stop
stop = True

def halten():
   time.sleep (2.6)

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
        if Anfang:
            stop = False
            
        
        
        
    # starte aufgabe 
    while stop == False:
        x = 300
        y = 600
        mouse.move(x, y, absolute=True)
        print("Maus wird gedrückt")
        mouse.press('left')
        print("Hält 2.4 sekunden")
        halten()
        mouse.release('left')
        
        if isWeiss([653, 347, 1142, 763]):
            stop = True
        
        while stop == True:
            time.sleep(1)
            print("Warte")
        
        x2 = 400
        mouse.move(x2, y, absolute=True)
        print("Maus wird gedrückt")
        mouse.press('left')
        print("Hält 2.4 sekunden")
        halten()
        mouse.release('left')
        
        while stop == True:
            time.sleep(1)
            print("Warte")
        
        x3 = 500
        mouse.move(x3, y, absolute=True)
        print("Maus wird gedrückt")
        mouse.press('left')
        print("Hält 2.4 sekunden")
        halten()
        mouse.release('left')
        
        while stop == True:
            time.sleep(1)
            print("Warte")
        
        
        x4 = 600
        mouse.move(x4, y, absolute=True)
        print("Maus wird gedrückt")
        mouse.press('left')
        print("Hält 2.5 sekunden")
        halten()
        mouse.release('left')

        if isWeiss([653, 347, 1142, 763]):
            stop = True