## This example filters out red color

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
    ## we return '_' as we don't care whether the frame has returned or not
    ## but we want the color filtering process to continue irrespective of that
    _, frame = cap.read()

    ## change the color space of the image as defining the HSV is easier than BGR
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## H(hue) = type of color
    ## S(saturation) =  darkness of that color starting from white upto that color
    ## V(value) = lightness of color starting from black upto that color

    ##define the limit for the color that need to be filtered
    ##                      h,s,v           
    lower_limit = np.array([0,100,100])
    upper_limit = np.array([250,255,255])

    ## creating mask by applying the limiting range to image
    ## px values within the range = ones i.e.whites and rest are blacked
    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    cv2.imshow('mask', mask)

    ## applying the mask to original image
    masked = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('filtered', masked)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()



    
    
