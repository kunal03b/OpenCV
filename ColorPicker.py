# Program to build Color picker using Trackbar.

import cv2
import numpy as np

def cross(x):
    pass

# create a blnk image
img = np.zeros((300,512,3),np.unit8)
cv2.namedWindow("Color picker")

# Create a switch to turn ON or OFF the color Picker
switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch, "Image picker", 0,1,cross)

# Create Trackbar for RGB color
cv2.getTrackbar("R","Color Picker", 0,255,cross)
cv2.getTrackbar("G","Color Picker", 0,255,cross)
cv2.getTrackbar("B","Color Picker", 0,255,cross)

while True:

    cv2.imshow("Color Picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # Get trackbar position
    s = cv2.getTrackbarPos(switch,"Color Picker")
    R = cv2.getTrackbarPos("R","Color Picker")
    G = cv2.getTrackbarPos("G","Color Picker")
    B = cv2.getTrackbarPos("B","Color Picker")

    if s == 0:
        img[:]= 0
    else:
        img = [R,G,B]

cv2.destroyAllWindows()




cv2.imshow(img)
cv2.destroyAllWindows()