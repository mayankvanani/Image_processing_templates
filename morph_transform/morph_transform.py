import cv2
import numpy as np

img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (300,300))


##morphological transformation is applied to binary images (generlly mask)
## applying bitwose_not considering the image input

## -- NOTE: NOISE IS BOTTOM RIGHT CORNER. LOOK FOR IT IN EVERY IMAGE ---- 

mask = cv2.bitwise_not(img)
cv2.imshow('mask', mask)

## erosion
## define a kernel that iterates over the image
kernel = np.ones((15,15), np.uint8)

## applying the erosion
## cv2.erode(image, kernel, iteration)
erosion = cv2.erode(mask, kernel, 1)
cv2.imshow('erosion', erosion)

## dialation
## define kernel --> already defined
dilation = cv2.dilate(mask, kernel, 1)
cv2.imshow('dilation', dilation)

## opening and closing is used  to eliminate background noise
## opening is erosion followed by dilation
## closing is dilation followed by erosion

## opening (USED TO REMOVE BACKGROUND NOISE)
## define kernel --> already defined
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)

## closing (USED TO REOMVE NOISE IN FOREGROUND)
## define kernel --> already defined
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)

## gradient
## gradient  = dialation - erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient',gradient)






