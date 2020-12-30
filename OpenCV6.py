import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# Syntax => 1-> Image, 2-> Two Coordinates in Tuple format, 3-> Color, 4-> Thickness
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a Rectangle With thickness of 5 Pax
# Syntax => 1-> Image, 2-> top-left corner and bottom-right corner, 3-> Color, 4-> Thickness
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Draw a Circle
# Syntax => 1-> Image, 2-> center coordinates, 3-> Radius, 4-> Color, 5-> Thickness
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Drawing Eclipse
# First ==> cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	)
# Second ==> cv.ellipse(img, box, color[, thickness[, lineType]]
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing a Polygon
# Syntax => cv.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]	)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

# Adding Text to Images
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)


cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()
