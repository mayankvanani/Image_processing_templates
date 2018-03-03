import numpy as np
import cv2


## MOG subtractor is gaussian mixture based model - GMM for foreground extraction
## Here  k-gaussian distribution is selected according.
## Has better adaptibility
## Has a default argument detectshadows=True , generally marked by gray pixels in images
## marking shadows decreases speed

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('MOG_subtractor', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
    
