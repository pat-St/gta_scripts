import mouse
import keyboard
import time
import pyautogui
from PIL import ImageGrab
import numpy as np

# screenshot_fenster=[x1, y1, x2, y2]
# farben=[r,g,b]
# bsp. if hatFarben([780, 347, 1142, 763],[200, 200,0]):
#           stop = False
def hatFarbe(screenshot_fenster,farbe):
    screenshot = ImageGrab.grab(bbox=screenshot_fenster,include_layered_windows=True,all_screens=True)
    erkennung = np.array(screenshot)
    #print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])
    #print("‐● Im Schalttafelmodus ●‐")
    #print("x:" + str(xlen) + " y:" + str(ylen))
    # erkennung[]
    midX = xlen //2
    midY = ylen //2

    #print("mitte: x:" + str(midX) + " y:" + str(midY))

    r = erkennung[midX,midY][0]
    g = erkennung[midX,midY][1]
    b = erkennung[midX,midY][2]
    
    fr = farbe[0]
    fg = farbe[1]
    fb = farbe[2]

    if fr <= r & fg <= g & fb <= b:
        print("‐●                                     ●‐")
        print("‐● Schalttafel wurde erfolgeich gelöst ●‐")
        print("‐●                                     ●‐")
        return True
    return False


def beendeScript():
    return hatFarbe([1860, 20, 1900, 70],[0,100,0])

def istGruen():
    return hatFarbe([1860, 20, 1900, 70],[0,100,0])


def hatErsterBlock():
    sx = 10
    sy = 10
    x1 = 1004
    x2 = x1+sx
    y1 = 580
    y2 = y1+sy
    ersterBlock = [x1, y1, x2, y2]
    gelb=[200, 200,0] 
    return hatFarbe(ersterBlock,gelb)

def hatZweiterBlock():
    sx = 10
    sy = 10
    x1 = 1050
    x2 = x1+sx
    y1 = 580
    y2 = y1+sy
    zweiterBlock = [x1, y1, x2, y2]
    orange=[200, 200,0]
    return hatFarbe(zweiterBlock,orange)

def hatDritterBlock():
    sx = 10
    sy = 10
    x1 = 1091
    x2 = x1+sx
    y1 = 580
    y2 = y1+sy
    dritterBlock = [x1, y1, x2, y2]
    gruen=[100,60,0]
    hatFarbe(dritterBlock,gruen)

def BruteForceKabelLoesung():
    # 3!=3*2*1=6
    for i in range(6):
        if not (hatErsterBlock() & hatZweiterBlock() & hatDritterBlock()):
            print("alle blöcke verteilt! sind verbunden")
            break
        # TODO nicer algorithmus    
    
def anfang(game_coords):
    screenshot = ImageGrab.grab(bbox=game_coords,include_layered_windows=True,all_screens=True)
    erkennung = np.array(screenshot)
    #print(str(screenshot))
    xlen = len(erkennung)
    ylen = len(erkennung[0])
    #print("Warte auf Schalttafel")

    #print("x:" + str(xlen) + " y:" + str(ylen))
    # erkennung[]
    midX = xlen //2
    midY = ylen //2

    #print("mitte: x:" + str(midX) + " y:" + str(midY))

    r = erkennung[midX,midY][0]
    g = erkennung[midX,midY][1]
    b = erkennung[midX,midY][2]
    if [51, 87, 105] == [r,g,b]:
        print("‐● Schalttafel wurde erkannt ●‐")
        return True
    return False

global stop
stop = True

duration=0.6

def warten():
   time.sleep (0.1)

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

counterLoop = 0

while True:
   
    counterLoop += 1
    if counterLoop < 2:
        print("‐●                       ●‐")
        print("‐● Warte auf Schalttafel ●‐")
        print("‐●                       ●‐")
        counterLoop = 0
       
    # warten bis eingabe dann start
    #print("Zum Starten q drücken und e zum Pausieren")
    while stop == True:
        time.sleep(0.5)
        if anfang([780, 347, 1142, 763]):
            stop = False
        
    while stop == False:
        print("‐● Im Schalttafelmodus ●‐")
      # Erster Durchgang
        if hatErsterBlock():
            pyautogui.moveTo (1011 ,586 )
            pyautogui.dragTo(872, 594, button='left', duration=duration) #Gelb / Blau
            pyautogui .mouseUp (button ='left')

        if beendeScript() or stop == True:
            break   

        if hatZweiterBlock():
            pyautogui.moveTo(1053 , 591)
            pyautogui.dragTo(874, 537, button='left', duration=duration)  # Orange / Pink
            pyautogui.mouseUp(button='left')

        if beendeScript() or stop == True:
            break 

        if hatDritterBlock():
            pyautogui.moveTo(1093, 592)
            pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Grün / Braun
            pyautogui.mouseUp(button='left')
            
        if beendeScript() or stop == True:
            break 

        if hatErsterBlock():
            pyautogui.moveTo(1011, 586)
            pyautogui.dragTo(874, 537, button='left', duration=duration)
            pyautogui.mouseUp(button='left')
            print("‐● Im Schalttafelmodus ●‐")

        if beendeScript() or stop == True:
            break    

        if hatZweiterBlock():
            pyautogui.moveTo(1053, 591)
            pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Orange / Braun
            pyautogui.mouseUp(button='left')
            
        
        if beendeScript() or stop == True:
            break 

        if hatDritterBlock(): 
            pyautogui.moveTo(1093, 592)
            pyautogui.dragTo(872, 597, button='left', duration=duration)  # Grün / Blau
            pyautogui.mouseUp(button='left')
            print("‐● Im Schalttafelmodus ●‐")

        if beendeScript() or stop == True:
            break

        if hatErsterBlock():
            pyautogui.moveTo(1011, 586)
            pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Gelb / Braun
            pyautogui.mouseUp(button='left') 

        if beendeScript() or stop == True:
            break 

        if hatZweiterBlock():
            pyautogui.moveTo(1053, 591)
            pyautogui.dragTo(872, 597, button='left', duration=duration)  # Orange / Blau
            pyautogui.mouseUp(button='left') 
            print("‐● Im Schalttafelmodus ●‐")

        if beendeScript() or stop == True:
            break 

        if hatDritterBlock():
            pyautogui.moveTo(1093, 592)
            pyautogui.dragTo(874, 537, button='left', duration=duration)  # Grün / Pink
            pyautogui.mouseUp(button='left') 
            
        