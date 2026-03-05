# Computer Vision Practice 01-03 (OpenCV)

This repository contains beginner-level OpenCV assignments for:

1. Loading an image and converting to grayscale.
2. Mouse painting with brush size control.
3. ROI (Region of Interest) selection by mouse drag.

The implementation stays simple on purpose for first-week practice.

## 1. Environment

- OS: Windows (tested in PowerShell)
- Python: 3.10+ recommended
- Libraries:
  - `opencv-python`
  - `numpy`

Install:

```bash
pip install opencv-python numpy
```

## 2. Project Files

- `practice01_load_gray.py`
- `practice02_paint_brush.py`
- `practice03_roi_select.py`
- `soccer.jpg`
- `girl_laughing.jpg`

## 3. Assignment Mapping (Requirement Check)

### Practice 01: Load + Grayscale + Side-by-side output

- Uses `cv.imread()` to load image.
- Uses `cv.cvtColor(..., cv.COLOR_BGR2GRAY)` for grayscale conversion.
- Uses `np.hstack()` to merge two images horizontally.
- Uses `cv.imshow()`, `cv.waitKey(0)`, `cv.destroyAllWindows()`.
- Includes defensive check (`if src is None: sys.exit(...)`).
- Handles channel mismatch before `hstack` by converting grayscale to BGR (`cv.COLOR_GRAY2BGR`).

### Practice 02: Painting + Brush size control

- Initial brush size: `5`.
- `+` or `=` increases size by `1`.
- `-` decreases size by `1`.
- Brush size range is clamped to `1..15`.
- Left click/drag draws blue.
- Right click/drag draws red.
- `q` closes the window.
- Keyboard input is processed in loop with `cv.waitKey(1)`.

### Practice 03: ROI selection and extraction

- Loads image and displays it.
- Uses `cv.setMouseCallback()` for mouse events.
- Drag draws rectangle (`cv.rectangle`) while selecting.
- On mouse release, selected ROI is cropped with NumPy slicing and shown in a separate window.
- `r` resets selection.
- `s` saves selected ROI using `cv.imwrite("roi.jpg", roi_img)`.
- Reverse drag direction is handled with `min/max` coordinate normalization.

## 4. How To Run

Run each script from project root:

```bash
python practice01_load_gray.py
python practice02_paint_brush.py
python practice03_roi_select.py
```

You can also pass an image path manually:

```bash
python practice01_load_gray.py soccer.jpg
python practice02_paint_brush.py girl_laughing.jpg
python practice03_roi_select.py soccer.jpg
```

## 5. Mid Results / Final Results (for GitHub report)

Create image captures and place them in `docs/images/`.

Recommended capture list:

- Practice 01
  - Mid: original image loaded
  - Final: `Original | Gray` combined output
- Practice 02
  - Mid: blue painting with default brush size
  - Mid: brush size changed (`+` or `-`)
  - Final: blue + red painted result
- Practice 03
  - Mid: dragging rectangle on source image
  - Final: ROI popup window
  - Final: saved file result (`roi.jpg`)

Example markdown blocks (replace file names with real captures):

```md
### Practice 01 Result
![p01-final](docs/images/p01_final.png)

### Practice 02 Result
![p02-mid](docs/images/p02_mid_brush.png)
![p02-final](docs/images/p02_final.png)

### Practice 03 Result
![p03-mid](docs/images/p03_mid_drag.png)
![p03-final-roi](docs/images/p03_final_roi.png)
```

## 6. Code Section For GitHub Page

For the assignment "code on GitHub page" requirement, include direct links:

- [practice01_load_gray.py](./practice01_load_gray.py)
- [practice02_paint_brush.py](./practice02_paint_brush.py)
- [practice03_roi_select.py](./practice03_roi_select.py)

Current code includes many line-by-line comments to match the "comment as much as possible" request.

## 7. GitHub Upload Steps

Run these commands in project root:

```bash
git init
git add .
git commit -m "Add OpenCV practice 01-03 with README and comments"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

If a repo already exists, skip `git init` and just use:

```bash
git add .
git commit -m "Update assignment README and practice code"
git push
```

## 8. Note

- Your local file is `girl_laughing.jpg` (with `g`), not `girl_laughin.jpg`.
- If needed, rename file or pass exact path explicitly when running scripts.
