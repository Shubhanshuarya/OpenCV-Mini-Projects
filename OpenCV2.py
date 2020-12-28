#Image Processing in OpenCV

import cv2 as cv
import sys

img = cv.imread('butterfly.jpg')

# print(img)

# If Image returns Null,Then Unable to read the image

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Display Window", img)

# Open Untill User Cancels the image
k = cv.waitKey(0)

# the image is written to a file if the pressed key was the "s"-key
if k == ord("s"):
    cv.imwrite('1.png', img)