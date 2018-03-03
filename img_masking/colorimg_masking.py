import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)

##defining mask

##defining black background
mask = np.zeros(img.shape[:2], dtype = np.uint8)

##defining white region
mask[100:300,100:700] = [255]

##applying mask
masked = cv2.bitwise_and(img,img, mask = mask)

cv2.imshow('masked', masked)
