import cv2
import numpy as np

img = cv2.imread('road_sign.jpg', cv2.IMREAD_COLOR)
rows, cols, depth = img.shape

## resizing for the sake of viewing various screen at a timeand compare
cols, rows = np.uint32([cols/2, rows/2])
img = cv2.resize(img, (cols,rows))
cv2.imshow('img',img)

## averaging
##cv2.blur(image, kernel_size)
avg_blur = cv2.blur(img, (5,5))
cv2.imshow('avg_blur', avg_blur)


## gaussian blurring
## cv2.GaussianBlur(image, kSize, standard deviation in Y direction = 0(usually))
##  gasussian kernel should be - ODD NUMBER
gauss = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('gauss', gauss)


## median blurring
## cv2.medianblur(image, ksize(an interger as ksize is integer * interger))
## ksize interger should bea odd interger
median = cv2.medianBlur(img, 5)
cv2.imshow('median',median)


## bilateral filter
##used to blur the image while keeping the edges unchanged
## slow filter if kernel size is large
##cv2.bilaterFilter(image, ksize, args(sigma space) )
bilateral1 = cv2.bilateralFilter(img, 25, 75, 75)
bilateral2 = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bilateral1',bilateral1)
cv2.imshow('bilateral2',bilateral2)


## filter-2D
##create a kernel for applying the filter
## np.ones( (kSize, dtype)/ (krows * scolums) )
kernel = np.ones((5,5), np.float32)/25

##cv2.filter2D(image, output_img, kernal)
filtered = cv2.filter2D(img, -1, kernel)
cv2.imshow('filtered',filtered)


















