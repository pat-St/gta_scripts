from utils.events import *

while True:
    # warten bis eingabe dann start
    print("Zum Starten x drücken d und e zum Pausieren")
    while stop == True:
        wait(2)

    while stop == False:
        print("E wird gehalten")
        keypress_time('e', sec=5)
        print("Taste wird losgelassen")
        wait(7)
