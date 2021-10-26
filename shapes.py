import cv2
import random
import numpy as np

img=np.zeros((512,512,3),np.uint8)#blank image
print(img.shape)
img[:]=0,0,0 #rop logic used to paint the screen blue completely
#if a certain part img[200:80,100;300]=255,0,0
cv2.line(img,(0,0),(100,100),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
for i in range(10):
    x=random.randint(20,500)
    y=random.randint(20,500)
    cv2.rectangle(img,(0,0),(x,y),(255,0,0),2)

cv2.circle(img,(100,100),50,(255,255,0))

cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_TRIPLEX,1,(0,150,0),3)
cv2.imshow("black",img)

cv2.waitKey(0)
