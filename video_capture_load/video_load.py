import cv2
import numpy as np

cap = cv2.VideoCapture('challenge.mp4')

## ret - returns 'true' or 'false' based on frame is captures or not
while True:
    ret, frame = cap.read()

    ##
    ## here do image processing stuff on frame
    ##

    cv2.imshow('frame', frame)

    

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

##releases the camera - switches it OFF
cap.release()
cv2.destroyAllWindows()
