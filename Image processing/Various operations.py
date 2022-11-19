# various image operations of pixel and coordinates i.e. shape,size,dtype,type,split.

import cv2
import numpy as np

image = input("Enter the path of image : ")
img = cv2.imread(image)
img = cv2.resize(img,(400,400)) #to set the size of the image

print("Shape = ",img.shape) #to return the no. of rows, columns and channels in the image
print("No. of pixels = ",img.size)

# -------------------------------------------TO split the image into multiple channels------------------------------------------
print(cv2.split(img))     #split function is used to split coloured image into separate single channel images.
b,g,r = cv2.split(img)
cv2.imshow("blue",b)   #to show the blue channel image
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("Original image",img)

# ---------------------------------------------To merge the splitted images-----------------------------------------------------
merged = cv2.merge((r,g,b))
cv2.imshow("Merged Image",merged)

merged2 = cv2.merge((b,g,r))
cv2.imshow("Merged Image",merged2)

# ----------------------------------------------Create Border of an image---------------------------------------------------------
border = cv2.copyMakeBorder(img,10,10,6,6,cv2.BORDER_CONSTANT,value=[26,55,7])
cv2.imshow("Bordered Image",border)

cv2.waitKey()
cv2.destroyAllWindows