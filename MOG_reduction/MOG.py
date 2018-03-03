import numpy as np
import cv2


## MOG subtractor is gaussian mixture based model - GMM for foreground extraction
##here  k- gaussian distribution is taken all over the image

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('MOG_subtractor', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
    
