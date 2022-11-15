# Low pass filter(LPS) are used to remove noise from images.
# High pass filter(HPS) are used to detect and finding edges in an image.
# various filters that we are going to discuss in this program are : homogeneous,blur(averaging),gaussian,median,bilateral.

import cv2
import numpy as np

image = input("Enter the path of the image: ")
img = cv2.imread(image)
img = cv2.resize(img,(400,600))
cv2.imshow("Original image", img)

# --------Homogeneous filter---------
kernel = np.ones((5,5),np.float32)/25     #kernel(a small matrix) is used to achieve the resulting image. Denominator = rows*columns.
h_filter = cv2.filter2D(img,-1,kernel)   #-1 is the depth of the filter.
cv2.imshow("Homogeneous filter", h_filter)


k = cv2.waitKey(1) & 0xFF
if k == 27:
    break
cv2.destroyAllWindows()
