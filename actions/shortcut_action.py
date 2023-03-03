from utils.events import *

while not quit_job():

    # warten bis eingabe dann start
    print("Das was du im Inventar benutzen willst lege es auf schnellzugriff 2")
    print("Zum Starten x drücken D und e zum Pausieren")
    while not active_job() and not quit_job():
        wait(2)

    counterLoop = 0
    while active_job():
        keypress_time('2', 0.2)
        wait(6)
        counterLoop += 1

        if counterLoop > 20:
            keypress_time('w', 1)
            keypress_time('s', 1)
            counterLoop = 0
