import sys

import cv2 as cv


start_x, start_y = -1, -1
is_dragging = False
original_img = None
display_img = None
roi_img = None


def mouse_callback(event: int, x: int, y: int, flags: int, param) -> None:
    global start_x, start_y, is_dragging
    global original_img, display_img, roi_img

    if event == cv.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_dragging = True

    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        display_img = original_img.copy()
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

    elif event == cv.EVENT_LBUTTONUP and is_dragging:
        is_dragging = False
        display_img = original_img.copy()
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

        x1, x2 = min(start_x, x), max(start_x, x)
        y1, y2 = min(start_y, y), max(start_y, y)

        if x2 > x1 and y2 > y1:
            roi_img = original_img[y1:y2, x1:x2]
            cv.imshow("ROI", roi_img)
        else:
            roi_img = None


def main() -> None:
    global original_img, display_img, roi_img

    original_img = cv.imread("images/soccer.jpg")
    if original_img is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    display_img = original_img.copy()

    win_name = "Select ROI"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, mouse_callback)

    print("Controls: drag ROI, 'r' reset, 's' save, 'q' quit")

    while True:
        cv.imshow(win_name, display_img)
        key = cv.waitKey(1) & 0xFF

        if key == ord("r"):
            display_img = original_img.copy()
            roi_img = None
            try:
                cv.destroyWindow("ROI")
            except cv.error:
                pass
        elif key == ord("s"):
            if roi_img is not None:
                cv.imwrite("roi.jpg", roi_img)
                print("Saved: roi.jpg")
            else:
                print("No ROI to save")
        elif key == ord("q"):
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
