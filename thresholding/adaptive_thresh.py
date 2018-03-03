import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (640,480))

##adaptive thresholding is used for images with varying illumination
## it is a kernel based method wherein we specify the the kernel size which\
## iterates over image applying the the threshold

##adaptive_thresh_mean
##adaptive threshold gaussian

##   NOTE: take care of image shape and kernel size

##cv2.threshold(image, maxVal, adaptive method, threshold_type, kernel_size, c)
## c - constant that is subracted from weighted mean a individual kernel
adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 85, 1)
adaptive_gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
cv2.imshow('adaptive_mean',adaptive_mean)
cv2.imshow('adaptive_gauss',adaptive_gauss)
