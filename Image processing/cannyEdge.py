# canny Edge Detection using OpenCV
# It is made with combination of five steps: Noise Detection(Gauss) -> Gradient calculation -> Non-maximum suppression -> Double Threshold -> Edge Tracking by Hysteresis

import cv2
import numpy as np

image = input("Enter the path of the image: ")
img = cv2.imread(image)
img = cv2.resize(img,(400,600))
Gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""canny_img = cv2.Canny(Gray_img,60,150)

cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",Gray_img)
cv2.imshow("Canny Image",canny_img)
"""
# Applying Canny Edge Detection using Trackbar
def cross(x):
    pass

cv2.namedWindow("Canny Image")
cv2.createTrackbar("Threshold Value","Canny Image",0,255,cross)

while True:
    pos = cv2.getTrackbarPos("Threshold Value","Canny Image")
    print(pos)
    output = cv2.Canny(Gray_img,pos,255)

cv2.waitKey(0)
cv2.destroyAllWindows()