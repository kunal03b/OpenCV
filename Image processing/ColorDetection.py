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

cv2.createTrackbar("Upper_H","Color Adjustment",0,255,cross)
cv2.createTrackbar("Upper_S","Color Adjustment",0,255,cross)
cv2.createTrackbar("Upper_V","Color Adjustment",0,255,cross)

