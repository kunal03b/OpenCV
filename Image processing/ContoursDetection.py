# Contours Detection using OpenCV

import cv2
import numpy as np

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass

# Create window for trackbar
cv2.namedWindow("Color Adjustment",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustment",(300,300))
cv2.createTrackbar("Thresh","Color Adjustment",0,255,nothing)

# Color Detection
cv2.createTrackbar("Lower_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_H","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustment",0,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustment",0,255,nothing)

while True:
    _,frame = cam.read()
    frame = cv2.resize(frame,(400,400))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # detecting Hand
    L_H = cv2.getTrackbarPos("Lower_H","Color Adjustment")
    L_S = cv2.getTrackbarPos("Lower_S","Color Adjustment")
    L_V = cv2.getTrackbarPos("Lower_V","Color Adjustment")

    U_H = cv2.getTrackbarPos("Upper_H","Color Adjustment")
    U_S = cv2.getTrackbarPos("Upper_S","Color Adjustment")
    U_V = cv2.getTrackbarPos("Upper_V","Color Adjustment")

    lower_bound = np.array([L_H,L_S,L_V])
    upper_bound = np.array([U_H,U_S,U_V])

    # Creating masked image
    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    # filter mask with image
    filtr = cv2.bitwise_and(frame,frame,mask = mask)

    mask1 = cv2.bitwise_not(mask)
    Thresh_M = cv2.getTrackbarPos("Thresh","Color Adjustment")
    ret,thresh = cv2.threshold(mask1,Thresh_M,255,cv2.THRESH_BINARY)
    dilata = cv2.dilate(thresh,(1,1),iterations=6)

    cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    frame = cv2.drawContours(frame,cnts,-1,(176,10,15),-4)

    cv2.imshow("result",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("Thresh",thresh)
    cv2.imshow("FIlter",filtr)

    k = cv2.waitKey(25) & 0xFF
    if k ==27:
        break

cv2.destroyAllWindows()

    
