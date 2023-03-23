# from utils.events import *
from utils.events import active_job, quit_job, sleep

print("This is a dummy job")
while not quit_job():
    # warten bis eingabe dann start
    print("Zum Starten x drücken p zum Pausieren")
    while not active_job() and not quit_job():
        wait(2)

    while active_job():
        print("Next round")
        sleep(2)
