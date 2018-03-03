import cv2
import numpy as np

img = cv2.imread('mario.jpg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)

##grayscaling
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## load the template
template = cv2.imread('mario_template.jpg', cv2.IMREAD_COLOR)

## note the width and height of template for drawing rectangle on matched template
w,h,channels = template.shape

## perform template matching
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

## percentage of matching 
threshold = 0.8

## returns a tuple of (x-coodrs) and (y-coords)
loc = np.where(result >= threshold)
##print(loc)

## zip is a iterator of tuple
## [::-1] in order to form coordinates (y,x) for opencv
for pt in zip(*loc[::-1]):
##    print(pt)
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)

cv2.imshow('final_image', img)
