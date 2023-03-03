from jobs.fishing import FishSymbolDetection
from utils.events import *

fishDetection = FishSymbolDetection(
    model_path="./assets/model2.pt",
    show_result=False
)
# model_path=".\\model.pt", show_result=False)
# fishDetection = FishSymbolDetection(model_path="assets\model.pt")xp
# fishDetection.use_screenshot_input([0, 20, 650, 700])
fishDetection.use_video_input("./assets/fischen_short.mp4")
# fishDetection.use_video_input(0)
while not quit_job():
    # warten bis eingabe dann start
    print("Zum Starten x drücken p zum Pausieren")
    while not active_job() and not quit_job():
        wait(2)

    if active_job():
        print("Angel wird ausgeworfen")
        start = None
        now = None
        keyclick('e')
        fishDetection.start()

    while active_job():
        fishsymbol = fishDetection.detect()
        if fishsymbol.detected():
            # Tire out the fish on the hook
            start = time.time()
            if fishsymbol.is_left():
                print("D wird gehalten")
                keypress('d')
                keyrelease('a')
            if fishsymbol.is_right():
                print("A wird gehalten")
                keypress('a')
                keyrelease('d')
        elif fishDetection.hasPullingBar():
            print("Fisch einziehen")
            keyrelease('a')
            keyrelease('d')
            while fishDetection.hasPullingBar():
                mousepress('left')
                wait(0.5)
            wait(3.2)
            mouserelease('left')
            wait(4)
            print("Fisch eingezogen")
            break
        else:
            if start and (time.time() - start) > 15:
                print("Zeit überschritten")
                break
        # print("Warte auf nächstes Bild")
        wait(1)
    fishDetection.stop()
    print("Alle Tasten werden losgelassen")
    keyrelease('a')
    keyrelease('d')
    mouserelease('left')
