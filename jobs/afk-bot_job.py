import random

from utils.events import *

input_actions = ['w', 'a', 'd']

while not quit_job():
    # warten bis eingabe dann start
    print("Zum Starten x drücken p zum Pausieren")
    while not active_job() and not quit_job():
        wait(2)

    while active_job():
        next_key = random.randint(0, len(input_actions))
        keypress(input_actions[next_key])
        wait((next_key+0.1)/10)
        keyrelease(input_actions[next_key])
