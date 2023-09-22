import mouse
import time
import keyboard
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

keyboard.add_hotkey('x', lambda: print(mouse.get_position()))
input(" ")
# keyboard.add_hotkey('e', lambda: stop_event())

# while True:

#     # warten bis eingabe dann start
#     print("Zum Starten x drücken dund e zum Pausieren")
#     while stop == True:
#         time.sleep(1)x
    
        
#     while stop == False:
#         time.sleep(2)
#         print(mouse.get_position())
