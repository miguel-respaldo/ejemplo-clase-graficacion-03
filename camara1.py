import numpy as np
import cv2

#Change Value of 2 to 0
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #in this line capture video from camarera and show color gray

    #canny = cv2.Canny(frame,100,200)#in this line canny capture video from camarera and show border in color withe
    #Canny code acept parameters : Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):

    # Display the resulting frame
    cv2.imshow('frame',gray)#Return configuration
    if cv2.waitKey(1) & 0xFF == ord('q'):#if you press "q" exit of aplication
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
