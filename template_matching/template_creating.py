import cv2
import numpy as np

img = cv2.imread('mario.jpg', cv2.IMREAD_COLOR)

## draw rectangle around the object that is to become template
## uncomment the below and try adjusting the coordinates
##cv2.rectangle(img, (114,41), (175,100), (255,255,255), 1)
cv2.imshow('main_img', img)

## cropping the ROI for previewing the template
crop = img[41:101, 113:175]
cv2.imshow('crop', crop)

##    TO SAVE --- UNCOMMENT THE BELOW LINE ---

##cv2.imwrite('mario_template.jpg', crop)
