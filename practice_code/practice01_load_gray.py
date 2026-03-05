import sys  # For command-line args and safe program exit.

import cv2 as cv  # OpenCV library.
import numpy as np  # Numpy library for array operations.


def main() -> None:
    # Use image path from CLI argument; fallback to the practice image.
    image_path = sys.argv[1] if len(sys.argv) > 1 else "soccer.jpg"

    # Read input image in BGR color mode.
    src = cv.imread(image_path, cv.IMREAD_COLOR)

    # Defensive check: stop safely when the image cannot be read.
    if src is None:
        sys.exit(f"Error: cannot read image -> {image_path}")

    # Convert BGR image to single-channel grayscale.
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Convert grayscale back to 3 channels so hstack dimensions match.
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # Stack original and grayscale image side-by-side.
    merged = np.hstack((src, gray_bgr))

    # Scale down only when merged image is larger than common screen size.
    max_width, max_height = 1400, 900
    h, w = merged.shape[:2]
    scale = min(max_width / w, max_height / h, 1.0)
    if scale < 1.0:
        merged_to_show = cv.resize(
            merged, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA
        )
    else:
        merged_to_show = merged

    # Show merged result in one window.
    cv.namedWindow("Original | Gray", cv.WINDOW_NORMAL)
    cv.imshow("Original | Gray", merged_to_show)

    # Wait until any key is pressed.
    cv.waitKey(0)

    # Close all OpenCV windows and release UI resources.
    cv.destroyAllWindows()


# Standard Python entry point.
if __name__ == "__main__":
    main()
