import sys  # For command-line args and safe exits.

import cv2 as cv  # OpenCV library.


# Global brush radius (assignment initial value: 5).
brush_size = 5

# Global image buffer for painting.
canvas = None


def draw(event: int, x: int, y: int, flags: int, param) -> None:
    """Mouse callback: left draws blue, right draws red."""
    global canvas
    global brush_size

    # Left click or left-button drag: draw filled blue circle.
    if event == cv.EVENT_LBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)

    # Right click or right-button drag: draw filled red circle.
    if event == cv.EVENT_RBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (0, 0, 255), -1)


def main() -> None:
    global canvas
    global brush_size

    # Use CLI image if provided; otherwise use practice image.
    image_path = sys.argv[1] if len(sys.argv) > 1 else "girl_laughing.jpg"

    # Load painting base image.
    canvas = cv.imread(image_path, cv.IMREAD_COLOR)

    # Defensive check: stop safely if loading failed.
    if canvas is None:
        sys.exit(f"Error: cannot read image -> {image_path}")

    # Create display window.
    win_name = "Painter"
    cv.namedWindow(win_name)

    # Bind mouse callback to the window.
    cv.setMouseCallback(win_name, draw)

    # Print controls in terminal.
    print("Controls: '+' or '=' increase size, '-' decrease size, 'q' quit")
    print(f"Brush size: {brush_size}")

    # Main event loop.
    while True:
        # Show updated canvas continuously.
        cv.imshow(win_name, canvas)

        # Read keyboard input every 1 ms.
        key = cv.waitKey(1) & 0xFF

        # Increase brush size with upper limit 15.
        if key in (ord("+"), ord("=")):
            brush_size = min(brush_size + 1, 15)
            print(f"Brush size: {brush_size}")

        # Decrease brush size with lower limit 1.
        elif key == ord("-"):
            brush_size = max(brush_size - 1, 1)
            print(f"Brush size: {brush_size}")

        # Quit when 'q' is pressed.
        elif key == ord("q"):
            break

    # Close all OpenCV windows.
    cv.destroyAllWindows()


# Standard Python entry point.
if __name__ == "__main__":
    main()
