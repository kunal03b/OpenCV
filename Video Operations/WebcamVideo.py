# Program to record video from webCam and save it to local

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame(500,500))
        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        # To exit the video capture. Here in waitkey 1 is used to for dynamic capture i.e. video and 0 is used for image capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
