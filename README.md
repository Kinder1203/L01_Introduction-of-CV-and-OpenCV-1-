# 컴퓨터 비전 OpenCV 실습 (01–03)

컴퓨터 비전 수업의 OpenCV 실습 과제 저장소입니다.  
총 3개의 실습으로 구성되어 있으며, 각 실습은 이미지 처리의 핵심 개념을 다룹니다.

---

## 환경 설정

| 항목 | 버전/도구 |
|---|---|
| Python | 3.10+ |
| 패키지 관리 | Anaconda (conda) |
| 주요 라이브러리 | `opencv-python`, `numpy` |

```bash
# conda 가상환경 생성 및 활성화
conda create -n cv python=3.10
conda activate cv

# 필요한 패키지 설치
pip install opencv-python numpy
```

## 실행 방법

프로젝트 루트(`computer_vison/`)에서 실행:

```bash
python practice_code/practice01_load_gray.py
python practice_code/practice02_paint_brush.py
python practice_code/practice03_roi_select.py
```

---

## 실습 01 — 이미지 불러오기 및 그레이스케일 변환

### 과제 설명

OpenCV를 사용하여 이미지를 불러오고, 그레이스케일로 변환한 뒤 원본과 나란히 표시하는 실습이다.

- `cv.imread()`로 이미지를 BGR 형식으로 불러온다
- `cv.cvtColor()`에 `cv.COLOR_BGR2GRAY`를 사용하여 그레이스케일로 변환
- `np.hstack()`으로 원본과 그레이스케일을 가로로 연결
- `cv.imshow()` + `cv.waitKey(0)`로 출력하고, 아무 키나 누르면 창이 닫힌다

### 핵심 코드 설명

```python
# BGR → 그레이스케일 변환 (단일 채널로 변환됨)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# 그레이스케일을 다시 3채널 BGR로 변환
# np.hstack()은 두 배열의 채널 수가 동일해야 하므로 필수
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# 원본(3채널)과 변환된 그레이(3채널)를 가로로 연결
merged = np.hstack((src, gray_bgr))
```

> **포인트**: OpenCV는 이미지를 RGB가 아닌 **BGR** 순서로 읽는다. 그레이스케일은 단일 채널이므로, `hstack`을 위해 `GRAY2BGR`로 3채널로 되돌려야 한다.

### 전체 코드

```python
import sys

import cv2 as cv
import numpy as np


def main() -> None:
    # BGR 형식으로 이미지를 불러온다
    src = cv.imread("images/soccer.jpg")

    # 이미지를 불러오지 못한 경우 종료
    if src is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    # BGR → 그레이스케일 변환
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # 그레이스케일을 3채널 BGR로 변환 (hstack 호환)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # 원본과 그레이스케일을 가로로 연결
    merged = np.hstack((src, gray_bgr))

    # 이미지가 화면보다 넓을 경우 축소
    max_width = 1400
    if merged.shape[1] > max_width:
        scale = max_width / merged.shape[1]
        merged = cv.resize(merged, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)

    # 결과 출력 후 아무 키나 누르면 종료
    cv.imshow("Original | Gray", merged)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
```

### 중간 결과물

<!-- 중간 결과 GIF를 여기에 넣으세요 -->
![practice01-mid](docs/images/practice01_mid.gif)

### 최종 결과물

<!-- 최종 결과 GIF를 여기에 넣으세요 -->
![practice01-final](docs/images/practice01_final.gif)

---

## 실습 02 — 페인팅 붓 크기 조절 기능 추가

### 과제 설명

마우스 입력으로 이미지 위에 붓질을 하고, 키보드 입력으로 붓 크기를 조절하는 실습이다.

- 초기 붓 크기는 **5**
- `+` 키: 붓 크기 1 증가 / `-` 키: 붓 크기 1 감소
- 붓 크기 범위: **최소 1, 최대 15**
- 좌클릭/드래그: **파란색** (BGR: 255,0,0) / 우클릭/드래그: **빨간색** (BGR: 0,0,255)
- `q` 키: 영상 창 종료
- `cv.setMouseCallback()`으로 마우스 이벤트 처리, `cv.circle()`로 원 그리기

### 핵심 코드 설명

```python
# 마우스 콜백 함수: 좌클릭 또는 좌클릭 드래그 시 파란색 원 그리기
if event == cv.EVENT_LBUTTONDOWN or (
    event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
):
    cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)

# 키보드 입력 처리: '+' → 붓 크기 증가 (최대 15), '-' → 감소 (최소 1)
if key == ord("+"):
    brush_size = min(brush_size + 1, 15)
elif key == ord("-"):
    brush_size = max(brush_size - 1, 1)
```

> **포인트**: `cv.waitKey(1)`로 1ms마다 키 입력을 확인하면서 루프를 돌린다. `EVENT_MOUSEMOVE`와 `EVENT_FLAG_LBUTTON`/`EVENT_FLAG_RBUTTON` 플래그를 조합하면 드래그 중의 연속 그리기가 가능하다.

### 전체 코드

```python
import sys

import cv2 as cv


brush_size = 5  # 초기 붓 크기
canvas = None


def draw(event: int, x: int, y: int, flags: int, param) -> None:
    """마우스 콜백: 커서 위치에 원을 그린다."""
    global canvas, brush_size

    # 좌클릭 또는 좌클릭 드래그 → 파란색
    if event == cv.EVENT_LBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)

    # 우클릭 또는 우클릭 드래그 → 빨간색
    if event == cv.EVENT_RBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (0, 0, 255), -1)


def main() -> None:
    global canvas, brush_size

    canvas = cv.imread("images/girl_laughing.jpg")
    if canvas is None:
        sys.exit("Error: cannot read image -> images/girl_laughing.jpg")

    win_name = "Painter"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, draw)

    print("Controls: '+' increase, '-' decrease, 'q' quit")
    print(f"Brush size: {brush_size}")

    while True:
        cv.imshow(win_name, canvas)
        key = cv.waitKey(1) & 0xFF

        if key == ord("+"):
            brush_size = min(brush_size + 1, 15)
            print(f"Brush size: {brush_size}")
        elif key == ord("-"):
            brush_size = max(brush_size - 1, 1)
            print(f"Brush size: {brush_size}")
        elif key == ord("q"):
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
```

### 중간 결과물

<!-- 중간 결과 GIF를 여기에 넣으세요 -->
![practice02-mid](docs/images/practice02_mid.gif)

### 최종 결과물

<!-- 최종 결과 GIF를 여기에 넣으세요 -->
![practice02-final](docs/images/practice02_final.gif)

---

## 실습 03 — 마우스로 영역 선택 및 ROI(관심 영역) 추출

### 과제 설명

이미지를 불러온 뒤 사용자가 마우스로 클릭-드래그하여 관심 영역(ROI)을 선택하고, 선택한 영역을 추출하는 실습이다.

- `cv.setMouseCallback()`으로 마우스 이벤트 처리
- 드래그 중 `cv.rectangle()`로 선택 영역을 시각화 (초록색 사각형)
- 마우스를 놓으면 해당 영역을 numpy 슬라이싱으로 잘라내서 별도 창에 출력
- `r` 키: 영역 선택 리셋, `s` 키: ROI 이미지 파일로 저장 (`cv.imwrite()`)
- `q` 키: 종료

### 핵심 코드 설명

```python
# 드래그 중: 매 프레임마다 원본을 복사하여 깨끗한 상태에서 사각형을 그린다
display_img = original_img.copy()
cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

# 마우스를 놓았을 때: 좌표를 정렬하고 numpy 슬라이싱으로 ROI 추출
x1, x2 = min(start_x, x), max(start_x, x)
y1, y2 = min(start_y, y), max(start_y, y)
roi_img = original_img[y1:y2, x1:x2]  # 영역 자르기
```

> **포인트**: `min`/`max`로 좌표를 정렬하기 때문에 어느 방향으로 드래그해도 올바른 영역이 추출된다. `original_img.copy()`로 매번 깨끗한 이미지에 사각형을 그리므로 이전 프레임의 사각형이 남지 않는다.

### 전체 코드

```python
import sys

import cv2 as cv


start_x, start_y = -1, -1  # 드래그 시작 좌표
is_dragging = False
original_img = None
display_img = None
roi_img = None


def mouse_callback(event: int, x: int, y: int, flags: int, param) -> None:
    """마우스 콜백: 클릭-드래그로 ROI를 선택한다."""
    global start_x, start_y, is_dragging
    global original_img, display_img, roi_img

    # 좌클릭: 시작 좌표 기록
    if event == cv.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_dragging = True

    # 드래그 중: 실시간 사각형 미리보기
    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        display_img = original_img.copy()
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)

    # 좌클릭 해제: ROI 추출
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
```

### 중간 결과물

<!-- 중간 결과 GIF를 여기에 넣으세요 -->
![practice03-mid](docs/images/practice03_mid.gif)

### 최종 결과물

<!-- 최종 결과 GIF를 여기에 넣으세요 -->
![practice03-final](docs/images/practice03_final.gif)
