# Practice 01: Load Image and Grayscale Conversion
# Uses OpenCV to load an image, convert it to grayscale,
# and display both side-by-side using np.hstack().

import sys  # provides sys.exit() for error handling

import cv2 as cv  # OpenCV library for image processing
import numpy as np  # NumPy for array operations (hstack)


def main() -> None:
    # Load the image in BGR format (OpenCV default)
    src = cv.imread("images/soccer.jpg")

    # Exit if the image could not be loaded
    if src is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    # Convert BGR image to single-channel grayscale using COLOR_BGR2GRAY
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # Convert grayscale back to 3-channel BGR so it can be stacked with the original
    # np.hstack requires both arrays to have the same number of channels
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # Concatenate original and grayscale images horizontally (side-by-side)
    merged = np.hstack((src, gray_bgr))

    # Resize the merged image if it is wider than 1400 pixels to fit the screen
    max_width = 1400
    if merged.shape[1] > max_width:
        scale = max_width / merged.shape[1]  # calculate the scaling factor
        merged = cv.resize(merged, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)

    # Display the merged image in a window titled "Original | Gray"
    cv.imshow("Original | Gray", merged)

    # Wait indefinitely until any key is pressed
    cv.waitKey(0)

    # Close all OpenCV windows
    cv.destroyAllWindows()


# Entry point: run main() only when executed directly
if __name__ == "__main__":
    main()
