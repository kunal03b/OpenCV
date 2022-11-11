# Program to build Color picker using Trackbar.

import cv2
import numpy as np

def cross(x):
    pass

# create a blnk image
img = np.zeros((300,512,3),np.unit8)
cv2.namedWindow("Image picker")

cv2.imshow(img)
cv2.destroyAllWindows()