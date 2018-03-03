'''
 histogram gives idea about intensity variation
 x-axis = 0 to 256 gray pixel values and y-axis = no. of pixels having corresponsding values
 0-256 values is not always true but generally we will do processing in gray images

 bins: b1 = [0,15] ; b2 = [16,31] ; b3 = [32, 47] and so on.. so it will show
       no. of pixel that fall under b1, b2, b3 etc. and hence there will be
       16 bins or 16 units on x axis instead of 256 distinct values of gray intensity

 dims: dimension of histogram i.e parameters that we want to collect on histogram
 dim = 1 means we will have only intensity variation vs pixel density in grayscale image

 range = The limits for the values to be measured. For grayscale, range = [0,255]

 for dim = 2, i.e. for color images we plot 3D histogram and we will have
 (binx, biny)

 for 3D histogram
 load image, split image into R, G, B values, calculate histogram for each channel and then plot it 
'''


## following is function of HISTOGRAM CALCULATION AND NOT HISTOGRAM PLOTTING

##cv2.calcHist(images, channels, mask, histSize, ranges[], hist[, accumulate]])

##images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
##channels : it is also given in square brackets. It is the index of channel for which we calculate histogram.
##        For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2]
##        to calculate histogram of blue, green or red channel respectively.
##mask : mask image. To find histogram of full image, it is given as "None".
##    But if you want to find histogram of particular region of image, you have to create a mask image for that
##    and give it as mask.
##histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
##ranges : this is our RANGE. Normally, it is [0,256].

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)

## using openncv to calculate histogram
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
## the above function just calculates histogram values and we need to run a for loop to plot it using plt function

## using numpy to calculate histogram
##np.histogram(img_1Darray, bins, ranges[])
hist= np.histogram(img.ravel(), 256, [0,255])

## np.bincount is 10X faster than np.histogram
##np.bincount = (img[1-D array], minlength = [minimum length of bins in output array])
hist_bincount = np.bincount(img.ravel(),minlength=256)

##plotting the calculated histogram
plt.plot(hist_bincount, color = 'black')  
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

