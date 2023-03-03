from PIL import Image, ImageGrab


def screen_capture(frame_size) -> Image:
    screenshot: Image = ImageGrab.grab(
        bbox=frame_size,
        all_screens=True)
    return screenshot.convert(mode="RGB")


def center_pixel(frame_size):
    screenshot: Image = screen_capture(frame_size)
    width, heigh = screenshot.size
    midW = width // 2
    midH = heigh // 2
    pixel = screenshot.getpixel((midW, midH))
    return pixel


def isWhite(frame_size):
    # https://docs.python.org/3/library/functions.html#all
    return all(i >= 250 for i in center_pixel(frame_size))


def isColor(frame_size, color):
    # true if
    #   abs(frame[r] - color[r]) < 5 and
    #   abs(frame[g] - color[g]) < 5 and
    #   abs(frame[b] - color[b]) < 5
    return all(
        abs(i-cc) < 5 for i, cc in zip(
            center_pixel(frame_size),
            color
        )
    )
