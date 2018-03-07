## this code can be tested on a red object (red hp mouse)

import cv2
import numpy as np 
from collections import deque

## deque is high-perfomance container datatypes and is used for remembering points 
## deque(maxlen= int) is the maximum length of elements in the list 
tracked_pts = deque(maxlen=10)


## font is for writing the tracked movement onto the image
## defining a functions to write on the image
def write_north(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'NORTH', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_south(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'SOUTH', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_east(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'EAST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_west(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'WEST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_northwest(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'NORTH-WEST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_southwest(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'SOUTH-WEST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_northeast(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'NORTH-EAST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_southeast(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'SOUTH-EAST', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	return text 

def write_stationary(imgsrc):
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = cv2.putText(imgsrc, 'STATIONARY', (0,30), font, 1, (0,0,255), 2, cv2.LINE_AA)
	text = cv2.putText(imgsrc, 'x:{}'.format(x_9), (0,60), font, 1, (0,0,255), 2, cv2.LINE_AA)
	text = cv2.putText(imgsrc, 'y:{}'.format(y_9), (0,90), font, 1, (0,0,255), 2, cv2.LINE_AA)

## decision is subtraction of succesive points to know the direction of travel
def decision():
	if dx > 50 and dy > 50:
		write_northwest(img)
		print('northwest')
	elif dx > 50 and dy < -50:
		write_southwest(img)
		print('southwest')
	elif dx < -50 and dy < -50:
		write_southeast(img)
		print('southeast')
	elif dx < -50 and dy > 50:
		write_northeast(img)
		print('northeast')
	elif dx > 50:
		write_west(img)
		print('west')
	elif dy > 50:
		write_north(img)
		print('north')
	elif dx < -50:
		write_east(img)
		print('east')
	elif dy < -50:
		write_south(img)
		print('south')
	else:
		write_stationary(img)
		



cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	cv2.imshow('original', frame)
	img = np.copy(frame)

	## color masking
	blur = cv2.GaussianBlur(frame, (3,3),0)
	hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	lower_limit = np.array([0,50,50])
	upper_limit = np.array([10,255,255])
	mask = cv2.inRange(hsv, lower_limit, upper_limit)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5,5))
	# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, (5,5))
	cv2.imshow('mask', mask)

	## finding contours in the mask
	_,contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	## initialising an empty array to iterate over
	pmtr_array = []
	for cnt in contours:
		perimeter = np.int32(cv2.arcLength(cnt, closed=True))
		pmtr_array.append(perimeter)
	
	## finding largest contour
	try:
		## finding contours with max perimeter
		max_perimeter = max(pmtr_array)
		## finding the index of maximum perimeter contour
		## and drawing contour if perimeter > threshold perimeter
		## also if perimeter > threshold perimeter, finding centroid of contours
		max_perimeter_index = pmtr_array.index(max_perimeter)
		if max_perimeter > 400:
			hull = cv2.convexHull(contours[max_perimeter_index])
			cv2.drawContours(img, [hull], 0, (0,255,255), 3)
			## finding the centroid of contour to track its movement
			M = cv2.moments(contours[max_perimeter_index])
			cx = int(M['m10']/ M['m00'])
			cy = int(M['m01']/ M['m00'])
			centroid = (cx, cy)
			tracked_pts.append(centroid)
			## initially when video is initialised, len(tracked_pts will be increasinf towards 1)
			## and hence we cannot do subtraction of 9th index and 0th index
			## hence if condition is used to threshold and start subtraction only when
			if len(tracked_pts) == 10:
				x_0 = (tracked_pts[0])[0]
				y_0 = (tracked_pts[0])[1]
				x_9 = (tracked_pts[9])[0]
				y_9 = (tracked_pts[9])[1]
				## computing dx and dy and performing decision
				dx = x_0 - x_9
				dy = y_0 - y_9
				print('dx: {}'.format(dx))
				print('dy: {}'.format(dy))
				## decisioning
				decision()
			else:
				pass					
		else:
			pass
	except Exception as e:
		pass






	cv2.imshow('object_tracking', img)
	

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
