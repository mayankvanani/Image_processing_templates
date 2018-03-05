import cv2
import numpy as np 


img = cv2.imread('shapes.jpg', cv2.IMREAD_COLOR)
im_copy = np.copy(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)

ret, thresh = cv2.threshold(blur, 8, 250, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh)

cont, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255), 3)
cv2.imshow('contours', img)


## ---------------------------- contour properties ------------------------------- 

## counter[1] is orange square in the image
cnt = contours[1]


## Moments
## useful for finding properties of contours like total intensity, centroid, info about its orientation
M = cv2.moments(cnt)
print (M)

## to extract useful info. need to perform operation
## centroid is given by: Cx = M10/M00 and Cy = M01/M00 i.e. centroid = (Cx, Cy)
## area = M00
## more info on wiki search cv2.moments
cx = int(M['m10']/ M['m00'])
cy = int(M['m01']/ M['m00'])
ar = int(M['m00'])
print('centroid cx from moment is: {}'.format(cx))
print('centroid cy from moment is: {}'.format(cy))
print('area from moment is: {}]'.format(ar))

## CONTOUR AREA
area = cv2.contourArea(cnt)
print('cv2.contourArea is: {}'.format(area))

## CONTOUR PERIMETER
perimtr = cv2.arcLength(cnt, closed = True)
print('cv2.arcLength: {}'.format(perimtr))

## CONTOUR APPROXIMATION
## estimates the contour to closest possible shape
## eg: suppose a contour doesn't give a perfect square,then it will estimate it to a perfect square
## epsilon = max distance from contour to approximated contour
## after defining epsilon apply the apprimation method
epsilon = 0.1*cv2.arcLength(cnt, closed=True)
## cv2.approxPolyDP(contour_index, epsilon, closed=True/False)
approx = cv2.approxPolyDP(cnt,epsilon, closed=True)
## now the approximated contour has altered dimension and hence appply cv2.drawcontour on the approximated
## contour to get perfect contour


## CHECKING THE CONVEXITY
## this func. returns True/False and tells if the curve is convex or not
## contours[10] == star in the image (not convex)
## contours[1] == square in the image (convex)
check = cv2.isContourConvex(contours[10])
print('Is star convex: {}'.format(check))
check = cv2.isContourConvex(contours[1])
print('Is square convex: {}'.format(check))

## CONVEX HULL
## it checks for convexity defects i.e. it corrects the bulged out curve
## hull returns list of points of the corrected contours and various parameter operation can be done.
## apply draw contours to see the result (here convex hull is applied to -- STAR)
hull = cv2.convexHull(contours[10])
cv2.drawContours(im_copy, [hull], 0, (255,0,0), 2)
cv2.imshow('convexhull',im_copy)

## BOUNDING RECTANGLE
## two types of bounding rectangle
## straight obunding reectangle - doesnot consider the rotation of the object
## and hence the area of bounding rect. is not minimum
## x,y are top left corner of rect while w,h are width and height
x,y,w,h = cv2.boundingRect(contours[10])
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255), 2)
##cv2.imshow('bounding_operation', img)

##rotated rectangle
## draws rect with minimum area (considers rotation of object)
## in img window, blue box around star = rotated and yellow = straight rectangle
rect = cv2.minAreaRect(contours[10])
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (255,0,0), 2)
##cv2.imshow('bounding_operation', img)

## BOUNDING CIRCLE
## initially we find the circumcircle using minEnclosingCircle - returns center and radius
## then we extract centre and radius of circle to be drawn and the pass it to the cv2.circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (0,255,255), 2)
##cv2.imshow('bounding_operation', img)

## BOUNDING ELLIPSE
## contours[7] == rectangle (around which bounding ellipse is drawn)
ellipse = cv2.fitEllipse(contours[7])
cv2.ellipse(img, ellipse, (0,255,255), 2)
cv2.imshow('bounding_operation', img)





