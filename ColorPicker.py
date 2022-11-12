# Program to build Color picker using Trackbar.

import cv2
import numpy as np

def cross(x):
    pass

# create a blank image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color picker")

# Create a switch to turn ON or OFF the color Picker
switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch, "Color picker", 0,1,cross)

# Create Trackbar for RGB color
cv2.createTrackbar("R","Color picker", 0,255,cross)
cv2.createTrackbar("G","Color picker", 0,255,cross)
cv2.createTrackbar("B","Color picker", 0,255,cross)

while True:

    cv2.imshow("Color picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  #To exit
        break
    
    # Get trackbar position
    s = cv2.getTrackbarPos(switch,"Color picker")
    R = cv2.getTrackbarPos("R","Color picker")
    G = cv2.getTrackbarPos("G","Color picker")
    B = cv2.getTrackbarPos("B","Color picker")

    if s == 0:
        img[:]= 0
    else:
        img[:] = [R,G,B]

cv2.destroyAllWindows()