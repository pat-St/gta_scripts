import mouse
import keyboard
import time
import pyautogui
from PIL import ImageGrab
import numpy as np



def isgrün(game_coords):
    screenshot = ImageGrab.grab(bbox=game_coords,include_layered_windows=True,all_screens=True)
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
    if [100] <= [g]:
        print("‐●                                     ●‐")
        print("‐● Schalttafel wurde erfolgeich gelöst ●‐")
        print("‐●                                     ●‐")
        return True
    return False

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
        pyautogui .moveTo (1011 ,586 )
        if isgrün([1860, 20, 1900, 70]):
            stop = True
            break
        if stop == True:
           break
        pyautogui.dragTo(872, 594, button='left', duration=duration) #Gelb / Blau
        if isgrün([1860, 20, 1900, 70]):
            stop = True
            break
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
            break
        if stop == True:
           break
        pyautogui .mouseUp (button ='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True  
        if stop == True:
           break    
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        pyautogui.moveTo(1053 , 591)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.dragTo(874, 537, button='left', duration=duration)  # Orange / Pink
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break   
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break     
        pyautogui.moveTo(1093, 592)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break 
        #print("‐● Im Schalttafelmodus ●‐")
        pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Grün / Braun
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True  
        if stop == True:
           break    
      
             # Zweiter durchgang
        time.sleep (0.1 )
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break    
        pyautogui.moveTo(1011, 586)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        print("‐● Im Schalttafelmodus ●‐")
        pyautogui.dragTo(874, 537, button='left', duration=duration)
        if isgrün([1860, 20, 1900, 70]):
            stop = True  # Gelb / Pink
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True  
        if stop == True:
           break       
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break    
        pyautogui.moveTo(1053, 591)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break 
        #print("‐● Im Schalttafelmodus ●‐") 
        pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Orange / Braun
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break        
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break   
        pyautogui.moveTo(1093, 592)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break 
        print("‐● Im Schalttafelmodus ●‐")
        pyautogui.dragTo(872, 597, button='left', duration=duration)  # Grün / Blau
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left')
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        
         # Dritter durchgang
        
        if stop == True:
           break    
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break   
        pyautogui.moveTo(1011, 586)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break 
        #print("‐● Im Schalttafelmodus ●‐") 
        pyautogui.dragTo(1055, 533, button='left', duration=duration)  # Gelb / Braun
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left') 
        if isgrün([1860, 20, 1900, 70]):
            stop = True  
        if stop == True:
           break      
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break    
        pyautogui.moveTo(1053, 591)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        print("‐● Im Schalttafelmodus ●‐")
        pyautogui.dragTo(872, 597, button='left', duration=duration)  # Orange / Blau
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left') 
        if isgrün([1860, 20, 1900, 70]):
            stop = True 
        if stop == True:
           break    
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break    
        pyautogui.moveTo(1093, 592)
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break 
        #print("‐● Im Schalttafelmodus ●‐")
        pyautogui.dragTo(874, 537, button='left', duration=duration)  # Grün / Pink
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break
        warten()
        if isgrün([1860, 20, 1900, 70]):
            stop = True
        if stop == True:
           break  
        pyautogui.mouseUp(button='left') 
        if isgrün([1860, 20, 1900, 70]):
            stop = True 