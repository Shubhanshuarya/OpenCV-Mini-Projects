import cv2

#Capture frames from a Video
cap = cv2.VideoCapture('Videos/Simple_Vechile_Detection.avi')
car_cascade = cv2.CascadeClassifier('Important_Files/cars.xml')
cv2.namedWindow('name', 0)
cv2.resizeWindow('name', 1000, 500)
#Loops runs if capturing has been Initialized
while True:
    #Reads frames from a Video
    _, frame = cap.read()

    #Convert to gray scale of each frames
    gray = cv2. cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Detect the cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    #to draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+y,y+h), (0,0,255), 2)

    #Display frames in a window
    cv2.imshow('name', frame)

    #Wait for ESC Key to Stop
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()