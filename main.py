import tkinter
import customtkinter



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root_tk = tkinter.Tk()
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def elektro(): #Elektro
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
def Ab(): # Angeln Bergbau
        import mouse
        import keyboard
        import time
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

        keyboard.add_hotkey('x', lambda: start_event())
        keyboard.add_hotkey('e', lambda: stop_event())

        while True:

            # warten bis eingabe dann start
            print("Zum Starten x drücken dund e zum Pausieren")
            while stop == True:
                time.sleep(2)

            
                
            while stop == False:

                #mouse.click('left')
                print("E wird gehalten")
            # time.sleep(6)
                pyautogui.keyDown('e')
                time.sleep(5)
                print("Taste wird losgelassen")
                pyautogui.keyUp('e', _pause=False)

                print("Warte bis nächste runde")
                time.sleep(7)
    



# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Angeln Bergbau", command=Ab)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app, text="Elektro gut", command=elektro)
button.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
switch_var = customtkinter.StringVar(value="on")

# def switch_event():
#         import mouse
#         import keyboard
#         import time
#         import pyautogui


#         global stop
#         stop = True

#         def start_event():eee
#             global stop
#             stop = False
#             print("Start")

#         def stop_event():
#             global stop
#             stop = True
#             print("Wird Pausiert")

#         keyboard.add_hotkey('x', lambda: start_event())
#         keyboard.add_hotkey('e', lambda: stop_event())

#         while True:

#             # warten bis eingabe dann start
#             print("Zum Starten x drücken dund e zum Pausieren")
#             while stop == True:
#                 time.sleep(2)

            
                
#             while stop == False:

#                 #mouse.click('left')
#                 print("E wird gehalten")
#             # time.sleep(6)
#                 pyautogui.keyDown('e')
#                 time.sleep(5)
#                 print("Taste wird losgelassen")
#                 pyautogui.keyUp('e', _pause=False)

#                 print("Warte bis nächste runde")
#                 time.sleep(7), switch_var.get()

# switch_1 = customtkinter.CTkSwitch(master=root_tk, text="CTkSwitch", command=switch_event,
#                                    variable=switch_var, onvalue="on", offvalue="off")
# switch_1.pack(padx=20, pady=10)

# #frame_1 = customtkinter.CTkFrame(master=app)
# #frame_1.pack(pady=20, padx=60, fill="both", expand=True)


app.mainloop()