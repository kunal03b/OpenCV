# Image Gradient is a gradient change in the color or intensity in an image.
# Methods to calculate image gradient : Laplacian Derivative, SobeLX, SobeLY.

import cv2
import numpy as np

#convert image into grayscale format
image = input("Enter the path of the image: ")
img = cv2.imread(image)
img = cv2.resize(img,(400,500))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# --------Laplacian Derivative----------
lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize=1)     #parameters are (img,data_type for -ve val,ksize)
lap = np.uint8(np.absolute(lap))    #used to remove the noise from the image.


# ------------------------SobeL Operations--------------------------
# SobeL operation is a joint Gaussian smoothing plus differentiation operation. It is more resistant to noise.
# parameters(img,type for -ve val,x = 1,y = 0,ksize)
# SobeLX focus on vertical lines. and SobeLY focus on horizontal lines.
sobelx = cv2.Sobel(img_gray,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img_gray,cv2.CV_64F,0,1)

cv2.imshow("Original image",img)
cv2.imshow("Gray Image",img_gray)
cv2.imshow("Laplacian Image",lap)
cv2.imshow("SobelX Image",sobelx)
cv2.imshow("SobelY Image",sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
