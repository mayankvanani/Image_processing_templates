import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)

##tp know the pixel value, just reference the img[pixel] to variable to get BGR values
px = img[100,100]
print (px)

##modify the pixel value
img[100,100] = [255,255,255]
print(px)

##defining ROI
roi = img[100:200, 100:300]

## changing the color of ROI(to white squared patch here)
img[100:200, 100:300] = [255,255,255]


##cut and psting roi in different place
sign_board = img[100:200, 350:450]
## img[0: 200-100, 0: 450-350]
img[0:100, 0:100] = sign_board









cv2.imshow('img',img)
