import cv2
import numpy as np 



## whilte truw is used as this program was developed in sublime text and required continuous iteration to 
## output the image continuously other wise it will flash and go away
## for python remove the while True loop and corrent the indentation syntax to run it in IDLE
img = cv2.imread('shapes.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('original',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


## find countours accepts binary image 
## blurring eliminates noise and threshold ouputs a binary image
blur = cv2.GaussianBlur(gray, (3,3), 0)
## the image whose contours is to be detected sjould be WHITE rest should be black
## cv2.findcontours modifies the source image, so in order to preserve src img, make a copy of img(thresh in this case)
## and then apply cv2.findContours
ret, thresh = cv2.threshold(blur, 8, 250, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh)

##findinf different contours in the image
## outputs contours  and hierarcy
## imgoutput, contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_TREE(retrieval mode), contour_approximation_method)
## usign cv2.CHAIN_APPROX_NONE will store all the points of contours inted APPROX_SIMPLE stores just 2 points that are necessary to 
## define a line and compresses it.
cont, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

## after finding contours we need to draw contours
## cv2.drawContours(src_img, contours, index_of_contour, linecolor, linethickness)
## index of contours = -1 (draws all the contours)
cv2.drawContours(img, contours, -1, (0,0,255), 3)
cv2.imshow('contours', img)

	





