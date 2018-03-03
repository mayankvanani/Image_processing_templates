import numpy as np
import cv2

img = cv2.imread('road_sign.jpg')

## ----------------------TIME COSTLY AND NOT STABLE------------------------

##cv2.rectangle(img, (160, 10), (270, 105), (255,255,255))
##cv2.imshow('img', img)

mask = np.copy(img)*0
## background and foreground model: just a numpy array predifined in grabcut algorithm
bgd_model = np.zeros((1,65), np.uint8)
fgd_model = np.zeros((1,65), np.uint8)

##define rectangle coordinates for the region to grabcut (crop)
## this recangle must contain all objects that you want to extract
rect = (160,10,270,105)

## cropping the ROI defined by rect
## img - input image
## mask - it is where we specify areas of background/foreground
## rect - coorinates of rectangle of the format (w,x,y,z)
## bgdmodel, fgdmodel - np arrays used by grabcut algorithm internally
## iterCount - no. of iteration the algorithm should run
## mode - cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK
cropped = cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 1, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2 | mask==0),0, 1).astype(uint64)

## to get more accurate result
## mark the area that you want in forgnd but have not appeared  = ones(white color)
## mark the area that you don't want in foregnd but have appeared = zeros (black color)

img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
