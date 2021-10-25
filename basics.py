import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)


cam=cv2.VideoCapture(0)
cam.set(3,680)#width
cam.set(4,440)#height
cam.set(10,50)#contrast
pic=cv2.imread("6484438.jpg")
blue=cv2.GaussianBlur(pic,(11,11),0)#more ksize more blur and always 0
canny=cv2.Canny(pic,100,100)#for edge detection and can change the value of threshold to reduce the edges by increasing the values
dilate=cv2.dilate(canny,kernel,iterations=1)#smoothing curves or oil mpainting effect or thickening the edges and increasing iterations increases the thickness
dil=cv2.dilate(pic,kernel,iterations=1)
cv2.imshow("blank",blue)
cv2.imshow("edges",canny)
cv2.imshow("dilate",dilate)
cv2.imshow("dilateorg",dil)



while True:
    rex,img=cam.read()
    if(rex==True):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("sample",gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release()

cv2.waitKey(0)
cv2.destroyAllWindows()