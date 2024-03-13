import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('RGB Trackbar')
cv.createTrackbar('Red', 'RGB Trackbar', 0, 255, nothing)
cv.createTrackbar('Green', 'RGB Trackbar', 0, 255, nothing)
cv.createTrackbar('Blue', 'RGB Trackbar', 0, 255, nothing)

cv.setTrackbarPos('Red', 'RGB Trackbar', 125)
cv.setTrackbarPos('Green', 'RGB Trackbar', 125)
cv.setTrackbarPos('Blue', 'RGB Trackbar', 125)

img = np.zeros((300, 512, 3), np.uint8)

while True:
    r = cv.getTrackbarPos('Red', 'RGB Trackbar')
    g = cv.getTrackbarPos('Green', 'RGB Trackbar')
    b = cv.getTrackbarPos('Blue', 'RGB Trackbar')


    cv.rectangle(img, (0, 0), (512, 300), (b, g, r), -1)
    cv.imshow('RGB Trackbar', img)

    if cv.waitKey(1) & 0xFF == 27:
        break
