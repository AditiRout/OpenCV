#low and high pass filter
import cv2
import numpy as np

img=cv2.imread("doodle.jpg")
kernal=np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])#max resultss if 5x5 matrix
kernal=kernal/sum(kernal)

img=cv2.filter2D(img,-1,kernal)
cv2.imshow("lowpassfilter",img)
cv2.waitKey(0)
cv2.imwrite("lowpassfilter.jpg",img)

#edge detection

kernel=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
kernel=kernel/(np.sum(kernel)if np.sum(kernel)!=0 else 1)
img_ = cv2.filter2D(img,-1,kernel)
cv2.imshow("highpassfilter",img_)
cv2.waitKey(0)
cv2.imwrite("highpassfilter.jpg",img_)

