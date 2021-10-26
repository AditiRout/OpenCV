import cv2
import numpy as np

img=cv2.imread("Frame 3.png")#use images with small dimensions..else wont work
imgHor=np.hstack((img,img))#to attah horizontally
imgpop=np.vstack((imgHor,imgHor))
imgV=np.vstack((img,img))

cv2.imshow("Vertical",imgV)
cv2.imshow("Horizontal",imgHor)
cv2.imshow("output",imgpop)

cv2.waitKey()