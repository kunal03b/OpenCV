# Video Operation using OpenCV

import cv2

vid1 = input("Enter the path of the video")
cap = cv2.VideoCapture(vid1)
print("cap",cap)

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame(500,500))
    # To convert Video to gray scale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("GrayScale Image",gray)
    cv2.waitKey(25)   #here 25 is the playback speed i.e. the less will be the value the more will be the speed of video
    # k = cv2.waitKey(25)
    # if k == ord('e'):
    #     break

cap.release()
cv2.destroyAllWindows()