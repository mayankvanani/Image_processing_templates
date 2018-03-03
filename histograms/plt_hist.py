## plt function calculates and plots the histogram

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
img = np.array(img)


##plt.hist(img.ravel(), bins_minlength, ranges = [])
##   .ravel returns a flattened array or otherwise called 1-D array
img_hist = plt.hist(img.ravel(), 256, [0,256])
plt.show()
