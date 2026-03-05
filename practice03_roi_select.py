import sys  # For command-line args and safe exits.

import cv2 as cv  # OpenCV library.


# Start point of drag rectangle.
start_x, start_y = -1, -1

# Drag state flag.
is_dragging = False

# Immutable original image buffer.
original_img = None

# Mutable display buffer for live rectangle preview.
display_img = None

# Last extracted ROI image buffer.
roi_img = None


def mouse_callback(event: int, x: int, y: int, flags: int, param) -> None:
    """Handle ROI rectangle selection by mouse drag."""
    global start_x, start_y, is_dragging
    global original_img, display_img, roi_img

    # Start drag on left mouse down.
    if event == cv.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_dragging = True

    # During drag: redraw from original image to avoid rectangle trails.
    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        display_img = original_img.copy()
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

    # End drag on left mouse up and extract final ROI.
    elif event == cv.EVENT_LBUTTONUP and is_dragging:
        is_dragging = False
        display_img = original_img.copy()
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

        # Normalize coordinates to support reverse drag direction.
        x_min, x_max = min(start_x, x), max(start_x, x)
        y_min, y_max = min(start_y, y), max(start_y, y)

        # Validate ROI size and show cropped result.
        if x_max > x_min and y_max > y_min:
            roi_img = original_img[y_min:y_max, x_min:x_max].copy()
            cv.imshow("ROI", roi_img)
        else:
            roi_img = None
            print("Invalid ROI size. Select again.")


def safe_close_window(win_name: str) -> None:
    """Close window only if it exists."""
    try:
        if cv.getWindowProperty(win_name, cv.WND_PROP_VISIBLE) >= 0:
            cv.destroyWindow(win_name)
    except cv.error:
        pass


def main() -> None:
    global original_img, display_img, roi_img

    # Use CLI image path if provided; otherwise use practice image.
    image_path = sys.argv[1] if len(sys.argv) > 1 else "soccer.jpg"

    # Load original image in BGR format.
    original_img = cv.imread(image_path, cv.IMREAD_COLOR)

    # Defensive check: exit safely when file load fails.
    if original_img is None:
        sys.exit(f"Error: cannot read image -> {image_path}")

    # Initialize display buffer.
    display_img = original_img.copy()

    # Create main window.
    win_name = "Select ROI"
    cv.namedWindow(win_name)

    # Bind mouse callback to ROI selection window.
    cv.setMouseCallback(win_name, mouse_callback)

    # Print keyboard controls.
    print("Controls: drag to select ROI, 'r' reset, 's' save, 'q' quit")

    # Main event loop.
    while True:
        # Keep showing the current display image.
        cv.imshow(win_name, display_img)

        # Read keyboard every 1 ms.
        key = cv.waitKey(1) & 0xFF

        # Reset selection and close ROI window.
        if key == ord("r"):
            display_img = original_img.copy()
            roi_img = None
            safe_close_window("ROI")
            print("Reset complete")

        # Save ROI only when valid ROI exists.
        elif key == ord("s"):
            if roi_img is not None and roi_img.size > 0:
                saved = cv.imwrite("roi.jpg", roi_img)
                if saved:
                    print("Saved: roi.jpg")
                else:
                    print("Save failed")
            else:
                print("No ROI to save.")

        # Quit loop.
        elif key == ord("q"):
            break

    # Close all windows.
    cv.destroyAllWindows()


# Standard Python entry point.
if __name__ == "__main__":
    main()
