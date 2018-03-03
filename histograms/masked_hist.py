import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic_2.jpg', cv2.IMREAD_GRAYSCALE)


##  Creating MASK

##creating black background of the shape of image[rows,cols] 
mask  = np.zeros(img.shape[:2],dtype = np.uint8)

## defining white part on blcack backgraound of our mask which we will be able
## to see in the final image
mask[100:300, 100:800] = 255

## applying MASK to image
## white part is visible of the final image
masked = cv2.bitwise_and(img, img , mask = mask)
cv2.imshow('masked', masked)


## calculate and plot histogram of masked image.
masked_hist = cv2.calcHist([img],channels=[0], mask=mask, histSize=[256], ranges=[0,255])
plt.plot(masked_hist)
plt.show()


