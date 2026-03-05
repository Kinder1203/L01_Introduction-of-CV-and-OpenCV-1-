# Computer Vision OpenCV Practice (01-03)

This README is organized for the assignment submission page.
It includes:
- assignment description
- intermediate result slots
- final result slots
- code links

## 1. Environment

- Python 3.10+
- `opencv-python`
- `numpy`

Install:

```bash
pip install opencv-python numpy
```

## 2. Run Commands

Run from project root (`computer_vison`):

```bash
python practice_code/practice01_load_gray.py
python practice_code/practice02_paint_brush.py
python practice_code/practice03_roi_select.py
```

## 3. Practice 01: Load Image + Grayscale Conversion

### Assignment Description

- Load an image with OpenCV.
- Convert the image to grayscale.
- Show original and grayscale images side-by-side.
- Main APIs: `cv.imread()`, `cv.cvtColor()`, `np.hstack()`, `cv.imshow()`, `cv.waitKey()`

### Intermediate Result (GIF Slot)

Put your GIF in `docs/images/` and keep this markdown:

```md
![practice01-mid](docs/images/practice01_mid.gif)
```

### Final Result (GIF Slot)

```md
![practice01-final](docs/images/practice01_final.gif)
```

### Code

- [practice01_load_gray.py](./practice_code/practice01_load_gray.py)

---

## 4. Practice 02: Paint Brush Size Control

### Assignment Description

- Paint on image using mouse input.
- `+` key increases brush size by 1.
- `-` key decreases brush size by 1.
- Brush size range: min 1, max 15.
- Left click/drag: blue, right click/drag: red.
- `q` key exits.

### Intermediate Result (GIF Slot)

```md
![practice02-mid](docs/images/practice02_mid.gif)
```

### Final Result (GIF Slot)

```md
![practice02-final](docs/images/practice02_final.gif)
```

### Code

- [practice02_paint_brush.py](./practice_code/practice02_paint_brush.py)

---

## 5. Practice 03: Mouse ROI Selection and Extraction

### Assignment Description

- Load image and select ROI by click-and-drag.
- Draw rectangle while dragging.
- On mouse release, crop ROI and show it in a separate window.
- `r` key resets selection.
- `s` key saves selected ROI.

### Intermediate Result (GIF Slot)

```md
![practice03-mid](docs/images/practice03_mid.gif)
```

### Final Result (GIF Slot)

```md
![practice03-final](docs/images/practice03_final.gif)
```

### Code

- [practice03_roi_select.py](./practice_code/practice03_roi_select.py)

---

## 6. Code Comment Checklist

- Function purpose comments are present.
- Mouse/keyboard handling comments are present.
- Basic error-handling comments are present.

## 7. Submission Checklist

- Assignment descriptions written.
- Intermediate GIF slots added.
- Final GIF slots added.
- Code links added.
