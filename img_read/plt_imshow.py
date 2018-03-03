import numpy as np
import cv2
import matplotlib.pyplot as plt

#                (           ,       1        )
img = cv2.imread('pic_1.jpg', cv2.IMREAD_COLOR)

## in matplotlib library, we NEED TO DO BGR to RGB conversion
## and then apply plt stuff
## as in matplotlib dtype is float32 while our images are 8 bit 3 channel data.

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


## using matplotlib to show img
## cmap is color map not a necessary argument
plt.imshow(img_RGB, cmap=plt.cm.gray , interpolation = 'bicubic')

##drawing lines over the image using pixel values
plt.plot([150,180], [200,260], 'c', linewidth = 5)
plt.show()


