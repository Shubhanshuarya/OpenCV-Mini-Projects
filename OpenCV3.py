import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot Open Camera")
    exit()

# Below 2 Lines Will return the size of Default Window
# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

############################################################
# If we want to set our own size of display window

ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # Capture Frame by Frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't recieve frame (Stream End?), Existing...")
        break

    # Operation on frame come here
    gray = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    # Displaying the resulting frame
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

# When Everything is Done, Release the Capture
cap.release()
cv.destroyAllWindows()
