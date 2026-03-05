import sys

import cv2 as cv


brush_size = 5
canvas = None


def draw(event: int, x: int, y: int, flags: int, param) -> None:
    global canvas
    global brush_size

    if event == cv.EVENT_LBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)

    if event == cv.EVENT_RBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (0, 0, 255), -1)


def main() -> None:
    global canvas
    global brush_size

    canvas = cv.imread("images/girl_laughing.jpg")
    if canvas is None:
        sys.exit("Error: cannot read image -> images/girl_laughing.jpg")

    win_name = "Painter"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, draw)

    print("Controls: '+' increase, '-' decrease, 'q' quit")
    print(f"Brush size: {brush_size}")

    while True:
        cv.imshow(win_name, canvas)
        key = cv.waitKey(1) & 0xFF

        if key == ord("+"):
            brush_size = min(brush_size + 1, 15)
            print(f"Brush size: {brush_size}")
        elif key == ord("-"):
            brush_size = max(brush_size - 1, 1)
            print(f"Brush size: {brush_size}")
        elif key == ord("q"):
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
