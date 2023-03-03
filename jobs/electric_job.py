from utils.events import *
from utils.screen_capture import *

# Mouse move duration
DURATION = 0.5

SUCCESS_GREEN = [0, 100, 0]
YELLOW = [250, 200, 2]
ORANGE = [200, 100, 20]
GREEN = [0, 160, 70]


def solved():
    return isColor([1860, 20, 1900, 70], color=SUCCESS_GREEN)


def alleBloeckeSindVerbunden():
    return not (
        hatErsterBlock() and
        hatZweiterBlock() and
        hatDritterBlock()
    )


def get_block(x1, y1):
    sx = 10
    sy = 10
    x2 = x1+sx
    y2 = y1+sy
    block_frame = [x1, y1, x2, y2]
    return block_frame


def hatErsterBlock():
    x1 = 1005
    y1 = 591
    ersterBlock = get_block(x1, y1)
    return isColor(ersterBlock, YELLOW)


def hatZweiterBlock():
    x1 = 1053
    y1 = 580
    zweiterBlock = get_block(x1, y1)
    return isColor(zweiterBlock, ORANGE)


def hatDritterBlock():
    x1 = 1091
    y1 = 580
    dritterBlock = get_block(x1, y1)
    return isColor(dritterBlock, GREEN)


def schalttafelErkannt(screenshot_fenster):
    return isColor(screenshot_fenster, [51, 87, 105])


def durchlauf1():
    print("‐● Löse mit 1. Durchlauf ●‐")
    if hatErsterBlock():
        mousedrag(1011, 586, 872, 594,  absolute=True,
                  duration=DURATION)  # Gelb / Blau

    if solved() or not active_job():
        return  # raus anstatt weiter

    if hatZweiterBlock():
        mousedrag(1053, 591, 874, 537,  absolute=True,
                  duration=DURATION)  # Orange / Pink

    if solved() or not active_job():
        return

    if hatDritterBlock():
        mousedrag(1093, 592, 1055, 533, absolute=True,
                  duration=DURATION)  # Grün / Braun


def durchlauf2():
    print("‐● Löse mit 2. Durchlauf ●‐")
    if hatErsterBlock():
        mousedrag(1011, 586, 874, 537, absolute=True, duration=DURATION)

    if solved() or not active_job():
        return  # raus anstatt weiter

    if hatZweiterBlock():
        mousedrag(1053, 591, 1055, 533, absolute=True,
                  duration=DURATION)  # Orange / Braun

    if solved() or not active_job():
        return

    if hatDritterBlock():
        mousedrag(1093, 592, 872, 597, absolute=True,
                  duration=DURATION)  # Grün / Blau


def durchlauf3():
    print("‐● Löse mit 3. Durchlauf ●‐")
    if hatErsterBlock():
        mousedrag(1011, 586, 1055, 533, absolute=True,
                  duration=DURATION)  # Gelb / Braun

    if solved() or not active_job():
        return  # raus anstatt weiter

    if hatZweiterBlock():
        mousedrag(1053, 591, 872, 597, absolute=True,
                  duration=DURATION)  # Orange / Blau

    if solved() or not active_job():
        return

    if hatDritterBlock():
        mousedrag(1093, 592, 874, 537, absolute=True,
                  duration=DURATION)  # Grün / Pink


while not quit_job():
    if not active_job():
        print("‐●                       ●‐")
        print("‐● Warte auf Schalttafel ●‐")
        print("‐●                       ●‐")

    # warten bis eingabe
    while not active_job() and not quit_job():
        wait(in_sec=0.5)
        if schalttafelErkannt([780, 347, 1142, 763]):
            _start_job()

    # loop bis gelöst wurde
    while active_job():
        wait(in_sec=0.5)
        if alleBloeckeSindVerbunden():
            _stop_job()
            break

        durchlauf1()

        if solved() or not active_job():
            break

        durchlauf2()

        if solved() or not active_job():
            break

        durchlauf3()

        if solved() or not active_job():
            break
