# 실습 03: 마우스로 영역 선택 및 ROI(관심 영역) 추출
# 이미지 위에서 클릭-드래그로 사각형 영역을 선택하고,
# 선택된 영역을 잘라내서 별도 창에 표시한다.
# 조작: 'r' 선택 초기화, 's' ROI 저장, 'q' 종료

import sys  # 에러 발생 시 프로그램 종료를 위한 모듈

import cv2 as cv  # OpenCV 이미지 처리 라이브러리


# 마우스 드래그 상태 추적을 위한 전역 변수
start_x, start_y = -1, -1  # 드래그 시작 좌표
is_dragging = False  # 드래그 중 여부

# 이미지 참조 변수
original_img = None  # 원본 이미지 (변경하지 않음)
display_img = None  # 화면에 표시할 작업용 이미지 (사각형 오버레이 포함)
roi_img = None  # 추출된 ROI 영역 (선택 없으면 None)


def mouse_callback(event: int, x: int, y: int, flags: int, param) -> None:
    # 마우스 콜백: 클릭-드래그로 ROI를 선택한다.
    global start_x, start_y, is_dragging
    global original_img, display_img, roi_img

    # 좌클릭: 시작 좌표를 기록하고 드래그 시작
    if event == cv.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_dragging = True

    # 드래그 중 마우스 이동: 실시간으로 사각형 미리보기 표시
    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        display_img = original_img.copy()  # 매 프레임마다 깨끗한 이미지로 초기화
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)  # 초록색 사각형

    # 좌클릭 해제: 선택 완료 후 ROI 추출
    elif event == cv.EVENT_LBUTTONUP and is_dragging:
        is_dragging = False
        display_img = original_img.copy()  # 깨끗한 이미지로 초기화
        cv.rectangle(display_img, (start_x, start_y), (x, y), (0, 255, 0), 2)  # 최종 사각형 그리기

        # 좌상단과 우하단 좌표 계산 (어느 방향으로 드래그해도 동작)
        x1, x2 = min(start_x, x), max(start_x, x)
        y1, y2 = min(start_y, y), max(start_y, y)

        # 선택 영역이 유효한 크기일 때만 ROI 추출
        if x2 > x1 and y2 > y1:
            roi_img = original_img[y1:y2, x1:x2]  # numpy 슬라이싱으로 영역 자르기
            cv.imshow("ROI", roi_img)  # 잘라낸 영역을 별도 창에 표시
        else:
            roi_img = None  # 유효하지 않은 선택, ROI 초기화


def main() -> None:
    global original_img, display_img, roi_img

    # BGR 형식으로 이미지를 불러온다
    original_img = cv.imread("images/soccer.jpg")

    # 이미지를 불러오지 못한 경우 에러 메시지 출력 후 종료
    if original_img is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    # 화면 표시용 작업 사본 생성 (원본은 그대로 보존)
    display_img = original_img.copy()

    # 이름이 지정된 창을 생성하고 마우스 콜백 등록
    win_name = "Select ROI"
    cv.namedWindow(win_name)
    cv.setMouseCallback(win_name, mouse_callback)  # 콜백 함수를 창에 연결

    # 사용법 출력
    print("Controls: drag ROI, 'r' reset, 's' save, 'q' quit")

    # 메인 루프: 화면 갱신 및 키보드 입력 처리
    while True:
        cv.imshow(win_name, display_img)  # 현재 표시 이미지로 창 갱신
        key = cv.waitKey(1) & 0xFF  # 1ms 대기 후 키 입력 캡처

        # 'r' 키: 선택 초기화 및 ROI 창 닫기
        if key == ord("r"):
            display_img = original_img.copy()  # 깨끗한 이미지로 복원
            roi_img = None  # 저장된 ROI 초기화
            try:
                cv.destroyWindow("ROI")  # ROI 창이 열려 있으면 닫기
            except cv.error:
                pass  # 창이 없을 경우 에러 무시
        # 's' 키: 현재 ROI를 JPEG 파일로 저장
        elif key == ord("s"):
            if roi_img is not None:
                cv.imwrite("roi.jpg", roi_img)  # ROI를 roi.jpg로 저장
                print("Saved: roi.jpg")
            else:
                print("No ROI to save")  # 저장할 ROI가 없음
        # 'q' 키: 루프 종료
        elif key == ord("q"):
            break

    # 모든 OpenCV 창을 닫는다
    cv.destroyAllWindows()


# 직접 실행할 때만 main() 호출
if __name__ == "__main__":
    main()
