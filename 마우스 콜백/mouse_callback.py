import cv2 as cv
import numpy as np
import random as rd

def draw_rect(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+50, y+50), (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.int8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_rect)

while True:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
