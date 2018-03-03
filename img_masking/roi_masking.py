import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)
rows, cols, channels = img.shape
print('rows = {}'.format(rows))
print('cols = {}'.format(cols))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

##defining black background
mask = np.copy(gray)*0

##defining points of polygon to mask
pts = np.array([[0,598],[958,598],[476+10,296],[476-10,296]])

##creating a polygon of white color and defining it on black background
mask = cv2.fillPoly(mask, [pts], (255,255,255))
print(mask.shape)

cv2.imshow('mask',mask)

##applying mask on color image
masked_color = cv2.bitwise_and(img,img, mask=mask)
cv2.imshow('masked_color',masked_color)

##applying mask on gray image
masked_gray = cv2.bitwise_and(gray,gray, mask=mask)
cv2.imshow('masked_gray',masked_gray)
