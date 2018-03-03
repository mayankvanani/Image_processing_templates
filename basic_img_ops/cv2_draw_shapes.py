import cv2
import numpy as np

img = cv2.imread('pic_2.jpg', cv2.IMREAD_COLOR)
print(img.shape)

##operation on image shape
## [n:]= indexing is [0,1,2...n]; it will start from 1 till end
##[:n] = indexing is [0,1,2...n]; it will start from starting till [n-1]
img_shape = img.shape
print(img_shape[:1])

## cv2 arguments of all function is (columns, rows)
##  line
##cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
img = cv2.line(img, (100,200), (200,400) ,color=[0,0,255] , thickness = 5)

##rectangle
##cv.rectangle(image, top-left corner, bottom-right corner, color[], thickness[])
img = cv2.rectangle(img, (10,10), (200,200), color = [0,255,0], thickness = 2)

##cv2.circle(img, center, radius, color[], thickness)
cv2.circle(img, (500,500), 30, color=[255,0,0], thickness = 2 )

## here the thickness is -1 hence the circle fills in the color
cv2.circle(img, (100,500), 10 , color = (255,255,0), thickness = -1)


##polygon
##define the points that you want to connect
pts = np.array( [[600,50],[500,200], [400,50], [600, 100]] ,np.int32)

##join the points
##cv2.polylines(img, set of points[],isClosed = T/F color[], thickness )
## isClosed is input flag given T- when polygons is closed figure orelse it wont connect first and last point of polygons 
cv2.polylines(img, [pts], True, color = [255,0,255], thickness = 3)


##writing text on an image
##define font
font = cv2.FONT_HERSHEY_SIMPLEX

##cv2.putText(img, text'', starting pt of text, font, size ,color,thickness of letters, anti-aliasing fuction)
cv2.putText(img, 'NICE!', (400, 300), font, 5, (255,255,255), 2, cv2.LINE_AA)











cv2.imshow('img',img)
