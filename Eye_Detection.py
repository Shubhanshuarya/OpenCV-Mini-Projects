import cv2

# Load the Cascade
eye_cascade = cv2.CascadeClassifier('Important_Files/haarcascade_eye.xml')

# To Capture video from Webcam
cap = cv2.VideoCapture(0)
while True:
    #Read the Frame
    _, img = cap.read()

    #Convert to GrayScale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Detect the faces
    faces = eye_cascade.detectMultiScale(gray, 1.1, 4)

    #Draw the Rectangle around each face
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #Display
    cv2.imshow("Image", img)

    #Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture Object
cap.release()