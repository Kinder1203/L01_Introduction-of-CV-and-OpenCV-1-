# 실습 02: 페인팅 붓 크기 조절 기능
# 마우스 입력으로 이미지 위에 붓질을 하며,
# 키보드(+/-)로 붓 크기를 조절한다. q키로 종료.

import sys  # 에러 발생 시 프로그램 종료를 위한 모듈

import cv2 as cv  # OpenCV 이미지 처리 라이브러리


# 전역 붓 크기, 초기값 5 (요구사항)
brush_size = 5

# 그림을 그릴 캔버스 이미지
canvas = None


def draw(event: int, x: int, y: int, flags: int, param) -> None:
    """마우스 콜백: 커서 위치에 원을 그린다."""
    global canvas
    global brush_size

    # 좌클릭 또는 좌클릭 드래그 -> 파란색 원 그리기 (BGR: 255,0,0)
    if event == cv.EVENT_LBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (255, 0, 0), -1)  # -1은 원 내부 채우기

    # 우클릭 또는 우클릭 드래그 -> 빨간색 원 그리기 (BGR: 0,0,255)
    if event == cv.EVENT_RBUTTONDOWN or (
        event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON)
    ):
        cv.circle(canvas, (x, y), brush_size, (0, 0, 255), -1)  # -1은 원 내부 채우기


def main() -> None:
    global canvas
    global brush_size

    # 페인팅 캔버스로 사용할 이미지를 불러온다
    canvas = cv.imread("images/girl_laughing.jpg")

    # 이미지를 불러오지 못한 경우 에러 메시지 출력 후 종료
    if canvas is None:
        sys.exit("Error: cannot read image -> images/girl_laughing.jpg")

    # 이름이 지정된 창을 생성하고 마우스 콜백 등록
    win_name = "Painter"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, draw)  # draw 함수를 마우스 이벤트에 연결

    # 사용법 및 현재 붓 크기 출력
    print("Controls: '+' increase, '-' decrease, 'q' quit")
    print(f"Brush size: {brush_size}")

    # 메인 루프: 화면 갱신 및 키보드 입력 처리
    while True:
        cv.imshow(win_name, canvas)  # 현재 캔버스 상태를 창에 표시
        key = cv.waitKey(1) & 0xFF  # 1ms 대기 후 키 입력 캡처

        # '+' 키: 붓 크기 1 증가, 최대 15로 제한
        if key == ord("+"):
            brush_size = min(brush_size + 1, 15)
            print(f"Brush size: {brush_size}")
        # '-' 키: 붓 크기 1 감소, 최소 1로 제한
        elif key == ord("-"):
            brush_size = max(brush_size - 1, 1)
            print(f"Brush size: {brush_size}")
        # 'q' 키: 루프 종료
        elif key == ord("q"):
            break

    # 모든 OpenCV 창을 닫는다
    cv.destroyAllWindows()


# 직접 실행할 때만 main() 호출
if __name__ == "__main__":
    main()
