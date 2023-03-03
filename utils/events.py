import time

import keyboard
import mouse

global active
active = False
global end_job
end_job = False

keyboard.add_hotkey('x', lambda: _start_job())
keyboard.add_hotkey('p', lambda: _stop_job())
keyboard.add_hotkey('q', lambda: _quit_job())


def active_job():
    # global function for running job indicator
    # False -> wait for start
    # True -> job is running
    global active
    return active


def quit_job():
    global end_job
    return end_job


def _start_job():
    global active
    active = True
    print("Start")


def _stop_job():
    global active
    active = False
    print("Wird Pausiert")


def _quit_job():
    global end_job
    end_job = True
    print("Wird Beendet")


def wait(in_sec=0.21):
    time.sleep(in_sec)


def keyclick(hotkey):
    keyboard.press_and_release(hotkey)


def keypress(hotkey):
    keyboard.press(hotkey)


def keyrelease(hotkey):
    keyboard.release(hotkey)


def keypress_time(hotkey, sec=1.0):
    keypress(hotkey)
    wait(sec)
    keyrelease(hotkey)


def mouseclick(button='left'):
    mouse.click(button)


def mousepress(button='left'):
    mouse.press(button)


def mouserelease(button='left'):
    mouse.release(button)


def mousemove(x, y, absolute=True):
    mouse.move(x, y, absolute)


def mousescroll(delta=1):
    mouse.wheel(delta)


def mousedrag(start_x, start_y, end_x, end_y, absolute=True, duration=0.5):
    mouse.drag(start_x, start_y, end_x, end_y, absolute, duration)


def mousepress_time(hotkey, sec=1.0):
    mousepress(hotkey)
    wait(sec)
    mouserelease(hotkey)
