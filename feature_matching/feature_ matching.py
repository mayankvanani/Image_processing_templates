import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bottle.bmp', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

## created template using these function for feature_matching
##crop = img[390:801, 100:351]
##cv2.imwrite('feature_temp.bmp', crop)

template = cv2.imread('feature_temp.bmp', cv2.IMREAD_COLOR)
template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)


## ---- Brute Force Matcher -----

##initiate ORB detector
orb = cv2.ORB_create()

##find keypoints and descriptor with ORB
kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(img, None)

##create BFmatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

## Match descriptors
matches = bf.match(des1, des2)

## sorting them in order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

## drawing first n no.of matches
img2 = cv2.drawMatches(template, kp1, img, kp2, matches[:50], 2)

plt.imshow(img2)
plt.show()


