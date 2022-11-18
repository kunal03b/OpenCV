# Image Pyramid in openCV
# Two types of image pyramid : Gaussian pyramid, Laplacian pyramid.

import cv2
import numpy as np

image = input("Enter the path of the image: ")
img = cv2.imread(image)
img = cv2.resize(img,(400,600))

# Gaussian Pyramid : PyramidUp & PyramidDDown
# Pyramid Down
pyDown1 = cv2.pyrDown(image)
pyDown2 = cv2.pyrDown(pyDown1)
# Pyramid Up
pyUP1 = cv2.pyrUp(pyDown1)
pyUP2 = cv2.pyrUp(pyUP1)

cv2.imshow("Original Image",img)
cv2.imshow("Pyramid Down 1",pyDown1)
cv2.imshow("Pyramid Down 2",pyDown2)
cv2.imshow("Pyramid Up 1",pyUP1)
cv2.imshow("Pyramid Up 2",pyUP2)

# # to perform this with loop:-
# imgCopy = cv2.copy(img)
# data = [imgCopy]
# for i in range(4):
#     imgCopy = cv2.pyrDown(imgCopy)
#     data.append(imgCopy)
#     cv2.imshow("Pyramid Down "+str(i),imgCopy)

cv2.waitKey(0)
cv2.destroyAllWindows()



