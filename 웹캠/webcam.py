import cv2 as cv

CAMERA_ID = 0

cam = cv.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print('카메라를 열 수 없습니다.')
    exit()

cv.namedWindow('WebCam')

while True:
    ret, frame = cam.read()
    cv.imshow('WebCam', frame)

    if cv.waitKey(10) >= 0:
        break

cam.release()
cv.destroyAllWindows()
