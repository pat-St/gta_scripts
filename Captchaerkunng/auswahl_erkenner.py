import time

import cv2 as cv
import mouse
import numpy as np
from PIL import Image, ImageGrab


def get_auswahl(print_file=False):
    screenshot = ImageGrab.grab(
        bbox=[0,0,1920,1080], include_layered_windows=True, all_screens=True)
    # screenshot = cv.imread("C:/Users/lukas/Pictures/Captchabilder/image.png")
    erkennung = np.array(screenshot)
    coord_first_selection = erkennung[430:480,940:975] #[955,448,963,455]
    coord_second_selection = erkennung[515:565,940:975] #[952,536,960,544]
    coord_third_selection = erkennung[607:657,940:975] #[953,628,961,636]

    # Erstelle in schwarzes Bild 
    text_seperator = cv.imread("D:/Wichtige sachen/repo/gta_scripts/Captchaerkunng/auswahltrenner.drawio.png")
    text_seperator_as_array = np.array(text_seperator)[:50,0:35,:3]
    # Einzelne Ausschnitte zusammekleben
    all_selection = coord_first_selection
    all_selection = np.concatenate((all_selection, text_seperator_as_array), axis=1)
    all_selection = np.concatenate((all_selection, coord_second_selection), axis=1)
    all_selection = np.concatenate((all_selection, text_seperator_as_array), axis=1)
    all_selection = np.concatenate((all_selection, coord_third_selection), axis=1)

    time.sleep(1)
    # TODO: für Lukas: Maus scroll 
    mouse.move(1136, 632, absolute=True)
    mouse.click("left")

    time.sleep(1)

    screenshot = ImageGrab.grab(
        bbox=[0,0,1920,1080], include_layered_windows=True, all_screens=True)
    # screenshot = cv.imread("C:/Users/lukas/Pictures/Captchabilder/image.png")
    erkennung = np.array(screenshot)
    coord_fourth_selection = erkennung[515:565,940:975] #[952,536,960,544]
    coord_fith_selection = erkennung[607:657,940:975] #[953,628,961,636]

    # Einzelne Ausschnitte zusammekleben
    # all_selection = all_selection
    all_selection = np.concatenate((all_selection, text_seperator_as_array), axis=1)
    all_selection = np.concatenate((all_selection, coord_fourth_selection), axis=1)
    all_selection = np.concatenate((all_selection, text_seperator_as_array), axis=1)
    all_selection = np.concatenate((all_selection, coord_fith_selection), axis=1)

    # if print_file:
    cv.imwrite('D:/Wichtige sachen/repo/gta_scripts/Captchaerkunng/image.png',all_selection)
    return True

if __name__ == "__main__":
    auswahl_zahlen_liste = get_auswahl(print_file=True)