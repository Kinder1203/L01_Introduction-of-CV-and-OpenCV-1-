# Practice 03: Mouse ROI (Region of Interest) Selection and Extraction
# Click and drag to select a rectangular area on the image.
# The selected region is cropped and displayed in a separate window.
# Controls: 'r' resets selection, 's' saves ROI to file, 'q' quits.

import sys  # provides sys.exit() for error handling

import cv2 as cv  # OpenCV library for image processing


# Global state for mouse drag tracking
start_x, start_y = -1, -1  # starting point of the drag
is_dragging = False  # True while the user is dragging

# Image references
original_img = None  # unchanged copy of the loaded image
display_img = None  # working copy shown on screen (with rectangle overlay)
roi_img = None  # extracted ROI region (None if nothing is selected)


def mouse_callback(event: int, x: int, y: int, flags: int, param) -> None:
    """Mouse callback: handles ROI selection via click-and-drag."""
    global start_x, start_y, is_dragging
    global original_img, display_img, roi_img

    # Left button pressed: record start coordinates and begin dragging
    if event == cv.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_dragging = True

    # Mouse move while dragging: draw a live rectangle preview
    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        display_img = original_img.copy()  # reset to clean image each frame
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)  # green rect

    # Left button released: finalize selection and extract ROI
    elif event == cv.EVENT_LBUTTONUP and is_dragging:
        is_dragging = False
        display_img = original_img.copy()  # reset to clean image
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)  # draw final rect

        # Calculate top-left and bottom-right corners (handle any drag direction)
        x1, x2 = min(start_x, x), max(start_x, x)
        y1, y2 = min(start_y, y), max(start_y, y)

        # Only extract ROI if the selected area has nonzero width and height
        if x2 > x1 and y2 > y1:
            roi_img = original_img[y1:y2, x1:x2]  # crop via numpy slicing
            cv.imshow("ROI", roi_img)  # display the cropped region
        else:
            roi_img = None  # invalid selection, clear ROI


def main() -> None:
    global original_img, display_img, roi_img

    # Load the image in BGR format
    original_img = cv.imread("images/soccer.jpg")

    # Exit if the image could not be loaded
    if original_img is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    # Make a working copy for display (original stays untouched)
    display_img = original_img.copy()

    # Create a named window and register the mouse callback
    win_name = "Select ROI"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, mouse_callback)  # attach callback to window

    # Print usage instructions
    print("Controls: drag ROI, 'r' reset, 's' save, 'q' quit")

    # Main loop: refresh display and handle keyboard input
    while True:
        cv.imshow(win_name, display_img)  # update the window with the current display
        key = cv.waitKey(1) & 0xFF  # wait 1ms and capture key press

        # 'r' key: reset the selection and close the ROI window
        if key == ord("r"):
            display_img = original_img.copy()  # restore clean image
            roi_img = None  # clear saved ROI
            try:
                cv.destroyWindow("ROI")  # close ROI window if open
            except cv.error:
                pass  # ignore error if the window was not open
        # 's' key: save the current ROI to a JPEG file
        elif key == ord("s"):
            if roi_img is not None:
                cv.imwrite("roi.jpg", roi_img)  # save ROI as roi.jpg
                print("Saved: roi.jpg")
            else:
                print("No ROI to save")  # nothing to save
        # 'q' key: exit the loop
        elif key == ord("q"):
            break

    # Close all OpenCV windows before exiting
    cv.destroyAllWindows()


# Entry point: run main() only when executed directly
if __name__ == "__main__":
    main()
