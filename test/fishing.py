import time

from jobs.fishing import FishSymbolDetection

fishDetection = FishSymbolDetection(
    model_path="./assets/model2.pt",
    show_result=True
)

fishDetection.use_video_input("./assets/fischen_short.mp4")

try:
    fishDetection.start()
    while True:
        fishsymbol = fishDetection.detect()
        if fishsymbol.detected():
            if fishsymbol.is_left():
                print("D wird gehalten")

            if fishsymbol.is_right():
                print("A wird gehalten")
        time.sleep(0.01)
finally:
    fishDetection.stop()
    print("stopped")
