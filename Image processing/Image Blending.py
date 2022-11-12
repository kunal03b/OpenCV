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

# ---------------------------------------Blending Image(Simple)--------------------------------
blend1 = cv2.add(img1,img2)
cv2.imshow("Blend 1",blend1)

# -----------------------------------------Blending Image with adjustments --------------------------------
blend2 = cv2.addWeighted(img1,0.4,img2,0.6,0)
cv2.imshow("Blend 2",blend2) 

cv2.waitKey(0)
cv2.destroyAllWindows()


# In addWeighted the sum of weight of all the images should be equal to 1. i.e. 0.4+0.6 = 1
# addWeighted(img1,wt1,img2,wt2,gama value)
# gama value varies from 0 to 100.