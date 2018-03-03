import cv2
import numpy as np

img = cv2.imread('alphabet.jpg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)

## grayscaling
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## corner detection algorithm
##cv2.goodFeaturesToTrack(gray, maxpoints, quality of detection, min distance)
## quality of detection < 1 (higher the quality, more significant corners detected)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 20)
corners = np.int0(corners)

## .ravel() returns a continuous flattened array

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('corner', img)
