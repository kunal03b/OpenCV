import cv2
import numpy as np

image = input("Enter the path of the image: ")
frame = cv2.imread(image)
frame = cv2.resize(frame,(600,400))

def cross(x):
    pass
cv2.namedWindow("Color Adjustment")

# Create Trackbar
cv2.createTrackbar("Lower_H","Color Adjustment",0,255,cross)
cv2.createTrackbar("Lower_S","Color Adjustment",0,255,cross)
cv2.createTrackbar("Lower_V","Color Adjustment",0,255,cross)

cv2.createTrackbar("Upper_H","Color Adjustment",255,255,cross)
cv2.createTrackbar("Upper_S","Color Adjustment",255,255,cross)
cv2.createTrackbar("Upper_V","Color Adjustment",255,255,cross)

# Binding the Trackbar
while True:
    hsv  = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H","Color Adjustment")
    l_s = cv2.getTrackbarPos("Lower_S","Color Adjustment")
    l_v = cv2.getTrackbarPos("Lower_V","Color Adjustment")

    u_h = cv2.getTrackbarPos("Upper_H","Color Adjustment")
    u_s = cv2.getTrackbarPos("Upper_S","Color Adjustment")
    u_v = cv2.getTrackbarPos("Upper_V","Color Adjustment")

    # Passing the lower and upper bound values
    lower_BV = np.array([l_h,l_s,l_v])
    upper_BV = np.array([u_h,u_s,u_v])

    # getting the masked image 
    mask = cv2.inRange(hsv,lower_BV,upper_BV)

    # filter mask with image
    res = cv2.bitwise_and(frame,frame,mask=mask)   #color will be reflected by mask variable as upper and lower bound values are stored in mask
    
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

cv2.destroyAllWindows()