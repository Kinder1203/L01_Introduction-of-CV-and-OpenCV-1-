import sys

import cv2 as cv
import numpy as np


def main() -> None:
    src = cv.imread("images/soccer.jpg")
    if src is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    merged = np.hstack((src, gray_bgr))

    max_width = 1400
    if merged.shape[1] > max_width:
        scale = max_width / merged.shape[1]
        merged = cv.resize(merged, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)

    cv.imshow("Original | Gray", merged)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
