import cv2
import numpy as np

##thresholding is always performed on GRAYSCALE image
img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)

##cv2.threshold(image, minVal, maxVal, threshold_type)
##usually for a low light image - minVal is 10-50
##for a properly lighted image - min val is 100-200
##pixel value within he interval =  1(binary)
##pixel values falling outside the interval = 0(binary)

 
retval, binary_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
retval, binary_inv_thresh = cv2.threshold(img, 150,255,cv2.THRESH_BINARY_INV)

## truncated thresholding alters the contrast of image while applying threshold 
retval, trunc_thresh = cv2.threshold(img, 50, 100, cv2.THRESH_TRUNC)

retval, tozero_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)
retval, tozero_inv_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('binary_thresh', binary_thresh)
cv2.imshow('binary_inv_thresh', binary_inv_thresh)
cv2.imshow('trunc_thresh', trunc_thresh)
cv2.imshow('tozero_thresh', tozero_thresh)
cv2.imshow('tozero_inv_thresh', tozero_inv_thresh)


