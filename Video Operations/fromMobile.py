# Video Capturing from Mobile's Camera
# for this you have to install IP camera in your mobile.

import cv2

camera = input("Enter IP address: ")
# path = input("Enter the path where you want to save the file: ")

cap = cv2.VideoCapture(0)
cap.open(camera)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter(path,fourcc,50.0,(700,700))    #output contain four parameters that are : name,codec,fps,resolution,color or grayscale.

print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # commented because frame already taken while saving video in above code
        frame = cv2.resize(frame(500,500))
        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        # output.write(frame)
        # To exit the video capture. Here in waitkey 1 is used to for dynamic capture i.e. video and 0 is used for image capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
# output.release()
cv2.destroyAllWindows()