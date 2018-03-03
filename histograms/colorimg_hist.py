## Algorithm ##
## read the image
## split the channels
## calculate histogram for each channels
## plot histogram for each channel



import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img', img)



## cv2.calcHist(img[], channel, mask, histogram_size/bins[], ranges[,])
## in opencv for BGR channels have
##                        B = [0]
##                        G = [1]
##                        R = [2]
hist_blue = cv2.calcHist([img], [0], mask = None, histSize = [256], ranges = [0,255])
hist_green = cv2.calcHist([img], [1], mask = None, histSize = [256], ranges = [0,255])
hist_red = cv2.calcHist([img], [2], mask = None, histSize = [256], ranges = [0,255])



##np.bincount
b, g, r = cv2.split(img)

nphist_blue = np.bincount(b.ravel(), minlength = 256)
nphist_green = np.bincount(g.ravel(), minlength = 256)
nphist_red = np.bincount(r.ravel(), minlength = 256)





##cv2.calcHist
plt.figure(1)
plt.plot(hist_blue, color = 'b')
plt.plot(hist_green, color ='g' )
plt.plot(hist_red, color = 'r')

##np.bincount
plt.figure(2)
plt.plot(nphist_blue, color = 'b')
plt.plot(nphist_green, color = 'g')
plt.plot(nphist_red, color = 'r')

plt.show()














