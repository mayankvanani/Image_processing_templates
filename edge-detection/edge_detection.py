import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)

## three types of gradient filters or high pass filter in opencv
## laplacian, sobel, scharr
## generally apply it to gray image

##sobel - resistant to noise
## kernel size = -1(3x3 scharr matrix) gives better result than kernel of size =(3 x 3))

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 1)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 1)
cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)

## laplacian filter
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('laplacian', laplacian)

## canny (widely used)
canny = cv2.Canny(img, 80, 200)
cv2.imshow('canny', canny)

