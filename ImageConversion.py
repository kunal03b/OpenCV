#Image Conversion from colorful to grayscale

import cv2

path = input("Enter the path of the image: ")

#convert image into grayscale (0)
img1 = cv2.imread(path,0)
img1 = cv2.resize(img1,(600,750))

# Display the resulting image
cv2.imshow("GrayScale Image",img1)

#To save the converted Image in Local
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("D:\\output.jpg",img1)
else:
    cv2.destroyAllWindows()