from utils.events import *


def mouse_movement(x, y):
    mousemove(x, y, absolute=True)
    wait()


while not quit_job():
    # warten bis eingabe dann start
    print("Zum Starten x drücken d und e zum Pausieren")
    while not active_job() and not quit_job():
        wait(1)

    while active_job():
        keypress_time("g", 1)
        wait()
        keypress_time("7", 1)
        wait()
        positions = [
            (940, 519),
            (865, 650),
            (913, 596),
            (940, 519),
        ]
        for x, y in positions:
            mouse_movement(x=x, y=y)
            mouseclick("left")
            wait()
            if not active_job():
                break
        keyboardclick("1")
        wait()
        mouse_movement(x=859, y=731)
        mouseclick("left")
        wait()
        if not active_job():
            break
        print("esc wird gedrückt")
        keypress_time('esc', 0.1)
        if not active_job():
            break
        wait()
        keypress_time('enter', 1)
        if not active_job():
            break
        wait()
        for i in range(9):
            mousescroll(50000)
        wait()
        keypress_time('w', 0.042)
        wait()
        keypress_time('enter', 0.01)
        keypress_time('esc', 0.1)
        wait(0.1)
        keypress_time('esc', 0.1)
        wait(1.1)
