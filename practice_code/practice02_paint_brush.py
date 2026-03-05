# Practice 02: Paint Brush with Size Control
# Uses mouse input to paint on an image.
# Keyboard controls: '+' increases brush, '-' decreases brush, 'q' quits.

import sys  # provides sys.exit() for error handling

import cv2 as cv  # OpenCV library for image processing


# Global brush size, starts at 5 as required
brush_size = 5

# Canvas image that will be drawn on
canvas = None


def draw(event: int, x: int, y: int, flags: int, param) -> None:
    """Mouse callback: draws circles on the canvas at the cursor position."""
    global canvas
    global brush_size

    # Left button click or left-button drag -> draw a blue circle (BGR: 255,0,0)
    if event == cv.EVENT_LBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)  # -1 fills the circle

    # Right button click or right-button drag -> draw a red circle (BGR: 0,0,255)
    if event == cv.EVENT_RBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (0, 0, 255), -1)  # -1 fills the circle


def main() -> None:
    global canvas
    global brush_size

    # Load the image to use as the painting canvas
    canvas = cv.imread("images/girl_laughing.jpg")

    # Exit if the image could not be loaded
    if canvas is None:
        sys.exit("Error: cannot read image -> images/girl_laughing.jpg")

    # Create a named window and register the mouse callback
    win_name = "Painter"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, draw)  # attach the draw function to mouse events

    # Print initial instructions and brush size
    print("Controls: '+' increase, '-' decrease, 'q' quit")
    print(f"Brush size: {brush_size}")

    # Main loop: refresh display and handle keyboard input
    while True:
        cv.imshow(win_name, canvas)  # update the window with the current canvas
        key = cv.waitKey(1) & 0xFF  # wait 1ms and capture key press

        # '+' key: increase brush size by 1, capped at 15
        if key == ord("+"):
            brush_size = min(brush_size + 1, 15)
            print(f"Brush size: {brush_size}")
        # '-' key: decrease brush size by 1, minimum is 1
        elif key == ord("-"):
            brush_size = max(brush_size - 1, 1)
            print(f"Brush size: {brush_size}")
        # 'q' key: exit the loop
        elif key == ord("q"):
            break

    # Close all OpenCV windows before exiting
    cv.destroyAllWindows()


# Entry point: run main() only when executed directly
if __name__ == "__main__":
    main()
