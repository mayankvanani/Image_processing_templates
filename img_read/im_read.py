import numpy as np
import cv2
import matplotlib as plt

## IMREAD_COLOR loads a colored image. Any transperenecy in image is neglected
img1 = cv2.imread('pic_1.jpg', cv2.IMREAD_COLOR)

##IMREAD_GRAYSCALE load a gray converted image
img2 = cv2.imread('pic_1.jpg', cv2.IMREAD_GRAYSCALE)

##IMREAD_UNCHANGED loads an image including alpha channel - opaqeness of image
img3 = cv2.imread('pic_1.jpg', cv2.IMREAD_UNCHANGED)

##instead of flags we can also pass integer 1 , 0 , -1 for respective modes
##eg:  img1 = cv2.imread('pic_1.jpg', 1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)



cv2.waitKey(0)
cv2.destroyAllWindows
