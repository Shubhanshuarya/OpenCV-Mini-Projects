import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

#Define Codec and Create VideoWriter Object

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Use Flip Code to Rotate the Camera
    frame  = cv.flip(frame, 1)

    #Write the flipped Frame
    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()