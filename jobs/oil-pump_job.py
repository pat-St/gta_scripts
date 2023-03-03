from utils.events import *
from utils.screen_capture import *

selection = input("boost? (y|N)")
if len(selection) > 0 and str(selection).lower() is 'y':
    IS_BOOST = True
else:
    IS_BOOST = False

while not quit_job():
    # warten bis eingabe dann start
    print("Zum Starten q drücken und e zum Pausieren")
    while not active_job() and not quit_job():
        wait(1)

    while active_job():
        for pump in [300, 400, 500, 600]:
            mousemove(pump, 600, absolute=True)
            mousepress_time(
                'left',
                sec=2.6 if IS_BOOST else 3.8
            )
            while isWhite([653, 347, 1142, 763]):
                wait(1)
                print("Warte")
