import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)

## creating mask
## defining black background
mask = np.zeros(img.shape[:2], dtype= np.uint8)

## defining white background
mask[300:500,100: 800] = 255

##applying mask to img
masked = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('img', img)
cv2.imshow('masked', masked)
