# Video Operation using OpenCV

import cv2

vid1 = input("Enter the path of the video")
cap = cv2.VideoCapture(vid1)
print("cap",cap)

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame(500,500))
    cv2.imshow("frame",frame)
    cv2.waitKey(25)
    # k = cv2.waitKey(25)
    # if k == ord('e'):
    #     break

cap.release()
cv2.destroyAllWindows()