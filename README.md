# Computer Vision OpenCV Practice (01–03)

This repository contains three OpenCV practice exercises from the Computer Vision course.
Each exercise demonstrates core image processing concepts with fully commented Python code.

## Environment

- Python 3.10+
- `opencv-python`
- `numpy`

```bash
pip install opencv-python numpy
```

## How to Run

Run from the project root (`computer_vison/`):

```bash
python practice_code/practice01_load_gray.py
python practice_code/practice02_paint_brush.py
python practice_code/practice03_roi_select.py
```

---

## Practice 01 — Load Image & Grayscale Conversion

### Description

- Load an image with `cv.imread()`.
- Convert to grayscale using `cv.cvtColor()` with `cv.COLOR_BGR2GRAY`.
- Display original and grayscale side-by-side using `np.hstack()`.
- `cv.imshow()` + `cv.waitKey(0)` to show the result; press any key to close.

### Intermediate Result

<!-- Place your intermediate GIF here -->
![practice01-mid](docs/images/practice01_mid.gif)

### Final Result

<!-- Place your final GIF here -->
![practice01-final](docs/images/practice01_final.gif)

### Code

- [practice01_load_gray.py](./practice_code/practice01_load_gray.py)

---

## Practice 02 — Paint Brush with Size Control

### Description

- Paint on an image using mouse input via `cv.setMouseCallback()`.
- Left click/drag draws in **blue**, right click/drag draws in **red**.
- `+` key increases brush size by 1, `-` key decreases by 1.
- Brush size range: min 1, max 15. Initial size: 5.
- `q` key exits.

### Intermediate Result

<!-- Place your intermediate GIF here -->
![practice02-mid](docs/images/practice02_mid.gif)

### Final Result

<!-- Place your final GIF here -->
![practice02-final](docs/images/practice02_final.gif)

### Code

- [practice02_paint_brush.py](./practice_code/practice02_paint_brush.py)

---

## Practice 03 — Mouse ROI Selection & Extraction

### Description

- Load an image and select a region of interest (ROI) by click-and-drag.
- A green rectangle is drawn while dragging (`cv.rectangle()`).
- On mouse release, the selected region is cropped (numpy slicing) and shown in a separate window.
- `r` key resets selection, `s` key saves the ROI via `cv.imwrite()`, `q` key exits.

### Intermediate Result

<!-- Place your intermediate GIF here -->
![practice03-mid](docs/images/practice03_mid.gif)

### Final Result

<!-- Place your final GIF here -->
![practice03-final](docs/images/practice03_final.gif)

### Code

- [practice03_roi_select.py](./practice_code/practice03_roi_select.py)
