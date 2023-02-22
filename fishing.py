import time

import cv2 as cv
# import keyboard
# import mouse
import numpy as np

# import pyautogui
# from PIL import ImageGrab

global stop
stop = True


def warten(inSec=0.21):
    time.sleep(inSec)


# def start_event():
#     global stop
#     stop = False
#     print("Start")


# def stop_event():
#     global stop
#     stop = True
#     print("Wird Pausiert")


# keyboard.add_hotkey('x', lambda: start_event())
# keyboard.add_hotkey('e', lambda: stop_event())


videostream_url = "./assets/fischen_short.mp4"
videostream = cv.VideoCapture(videostream_url)

while True:
    ret, frame = videostream.read()
    if not ret:
        print("Non frame detected. End of stream")
        break
    cv.imshow('frame', frame)
    key_input = cv.waitKey(30) & 0xff
    if key_input == 27:
        break
    warten(0.01)
# print("Warte bis nächste runde")
cv.destroyAllWindows()
