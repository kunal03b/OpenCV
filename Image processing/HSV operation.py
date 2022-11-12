# HSV stands for Hue Saturation Value
# Program to detect colors in an image

import cv2
import numpy as np

image = input("Enter the path of an image: ")
frame = cv2.imreade(image)
bgrUp = input("Enter the upper bgr value of the color: ")
bgrLw = input("Enter the lower bgr value of the color: ")

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    U_V = np.array([bgrUp])   #upper and lower value will be given in the form of array.
    L_V = np.array([bgrLw])
    # Creating Mask
    mask = cv2.inRange(hsv, L_V, U_V)

    # Filter mask with Image
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

cv2.destroyAllWindows()




