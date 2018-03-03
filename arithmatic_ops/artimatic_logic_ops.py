import cv2
import numpy as np

img1 = cv2.imread('graph_1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('graph_2.jpg', cv2.IMREAD_COLOR)


####for adding image shape must be same
img1 = cv2.resize(img1, (600,400), interpolation = cv2.INTER_CUBIC)
img2 = cv2.resize(img2, (600,400), interpolation = cv2.INTER_CUBIC)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

## simple adding images superimposes one over the other
add = img1 + img2
cv2.imshow('add', add)

##cv2.add - adds the individual pixel value
##(100,160,130) + (10, 40, 225) = (110,200,355)....translated to (110,200,355)
cv_add = cv2.add(img1, img2)
cv2.imshow('cv_add',cv_add )

##adding images based on their weights
## weights of images added should sum upto 1
##cv2.addWeighted(img1, correspoding weight, img2, corres. weight, bias )
add_weights = cv2.addWeighted(img1, 0.8, img2, 0.2, 0 )
cv2.imshow('add_weights', add_weights)





