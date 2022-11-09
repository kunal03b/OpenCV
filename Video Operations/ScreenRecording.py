#  Program to record the screen and save it to the files.

import cv2
import pyautogui as pa
import numpy as np


# creating resolution
res = pa.size()

path = input("Enter the path to save the recorded video: ") + input("Enter the file name: ")
# fixing the frame rate...more the frame rate of the recorded video higher will be the speed
fps = 30.0

# to save into the file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(path,fourcc,fps,res)

# recording module
cv2.namedWindow('Live Recording',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live Recording',(400,400))


while True:
    img = pa.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow('Live Recording',f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output.release()
cv2.destroyAllWindows()
