# Image blending using OpenCV

import cv2
import numpy as np

image1 = input("Enter the Path of 1st image: ")
img1 = cv2.imread(image1)
img1 = cv2.resize(img1,(400,600))
image2 = input("Enter the Path of 2nd image: ")
img2 = cv2.imread(image2)
img2 = cv2.resize(img2,(400,600))

cv2.imshow("Image 1",img1)
cv2.imshow("image 2",img2)

# ---------------------------------------Blending Image--------------------------------
blend1 = cv2.add(img1,img2)
cv2.imshow("Blend 1",blend1)

cv2.waitKey(0)
cv2.destroyAllWindows()