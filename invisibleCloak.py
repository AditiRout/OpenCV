# DataFlair Invisible Cloak project using OpenCV.
import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
time.sleep(2)     
background = 0
for i in range(50):
    ret, background = cap.read()
while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([50, 80, 50])     
    upper_bound = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)
    #cv2.imshow("invisible",mask)
    cloak=cv2.bitwise_and(background,background,mask)
    # create inverse mask 
    inverse_mask = cv2.bitwise_not(mask)  

    # Apply the inverse mask to take those region of the current frame where cloak is # not present 
    current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    final=cv2.add(cloak,current_background)
    cv2.imshow("window",final)
    k=cv2.waitKey(1)
    if k=='q':
        break

cap.release()
cv2.destroyAllWindows()
