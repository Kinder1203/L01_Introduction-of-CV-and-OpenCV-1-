# 실습 01: 이미지 불러오기 및 그레이스케일 변환
# OpenCV를 사용하여 이미지를 불러오고, 그레이스케일로 변환한 뒤,
# np.hstack()을 이용해 원본과 나란히 출력한다.

import sys  # 에러 발생 시 프로그램 종료를 위한 모듈

import cv2 as cv  # OpenCV 이미지 처리 라이브러리
import numpy as np  # NumPy 배열 연산 (hstack에 사용)


def main() -> None:
    # BGR 형식으로 이미지를 불러온다 (OpenCV 기본 색상 순서)
    src = cv.imread("images/soccer.jpg")

    # 이미지를 불러오지 못한 경우 에러 메시지 출력 후 종료
    if src is None:
        sys.exit("Error: cannot read image -> images/soccer.jpg")

    # BGR 이미지를 단일 채널 그레이스케일로 변환 (COLOR_BGR2GRAY 사용)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # 그레이스케일을 다시 3채널 BGR로 변환 (hstack 시 채널 수가 동일해야 함)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # 원본 이미지와 그레이스케일 이미지를 가로로 연결 (나란히 표시)
    merged = np.hstack((src, gray_bgr))

    # 합쳐진 이미지가 화면보다 넓을 경우 1400px 기준으로 축소
    max_width = 1400
    if merged.shape[1] > max_width:
        scale = max_width / merged.shape[1]  # 축소 비율 계산
        merged = cv.resize(merged, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)

    # "Original | Gray" 제목의 창에 합쳐진 이미지를 출력
    cv.imshow("Original | Gray", merged)

    # 아무 키나 누를 때까지 대기
    cv.waitKey(0)

    # 모든 OpenCV 창을 닫는다
    cv.destroyAllWindows()


# 직접 실행할 때만 main() 호출
if __name__ == "__main__":
    main()
