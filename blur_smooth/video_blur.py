## this is in continuation with color filtering program
## This example filters out red color

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)      
    lower_limit = np.array([0,100,100])
    upper_limit = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    cv2.imshow('mask', mask)
    masked = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('filtered', masked)

    ##for smoothing the image we apply kernel based method that iterates over the image
    ##the center of the kernel is called anchor point where the average value of the kernel pixels are applied

    ##defining the kernel
    ## np.ones( (kSize, dtype)/ (krows * kcolums) )
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(masked, -1, kernel)
    cv2.imshow('smoothed', smoothed)

    ##here various filters can be applied
    ## look examples in img_blur.py in blur_smooth folder

    
    
    
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()



    
    
