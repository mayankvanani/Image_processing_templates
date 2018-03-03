## here we super impose the python logo on graph
import cv2
import numpy as np

img1 = cv2.imread('py_logo.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('graph_1.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

rows, cols, channels = img1.shape
print('rows = ', rows)
print('cols = ', cols)

##first we need to create a mask for py_logo
##as we want only logo and not the background appearing when superimposing
## hence mask is created for logo = white and background  = black
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)

##since we now have the mask, we need to define its background and forground
##its background will be extracted from graph_1
##its foreground would be py_logo

##defining the background for the mask

## background = the roi of main image on which we wish to superimpose the logo
##background should be of the of the same size of the image that we want to superimpose
##here the logo is [256,256], hence the bgnd should have same rows and colums
roi = img2[100:(100+rows), 150:(150+cols)]
cv2.imshow('roi', roi)

##filling the background of the mask
bgnd = cv2.bitwise_and(roi, roi, mask = mask)
cv2.imshow('bgnd', bgnd)


##defining the foreground
mask_inv = cv2.bitwise_not(mask, mask=None)
cv2.imshow('mask_inv', mask_inv)

##filling the color in mask_inv ans this is our foreground
fgnd = cv2.bitwise_and(img1, img1, mask= mask_inv)
cv2.imshow('fgnd',fgnd)

##adding the foreground and background will give the image that will be superimposed
imposing_img = cv2.add(bgnd,fgnd)
cv2.imshow('imposing_img',imposing_img)


##changing the pixel values of the main image --> superimposing image
img2[100:(100+rows), 150:(150+cols)] = imposing_img
cv2.imshow('final_image', img2)




















