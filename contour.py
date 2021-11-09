import cv2
import numpy as np


def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#to get outer details
    for c in contours:
        area=cv2.contourArea(c)
        print(area)#gives area
        cv2.drawContours(imgContour,c,-1,(255,0,0),3)#-1 to get all contours
        #to check for minimum area
        if area>2000:
             cv2.drawContours(imgContour,c,-1,(0,255,0),3)
             peri=cv2.arcLength(c,True)
             print(peri)
             approx=cv2.approxPolyDP(c,0.02*peri,True)#to get corner points
             #print(approx)
             print(len(approx))#total no.of points for a particular 
             objCor=len(approx)
             x,y,w,h=cv2.boundingRect(approx)
             if objCor==3: 
                objecttype="Tri"
             elif objCor==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objecttype="square"
                else :
                    objecttype="rect"
             else:
                objecttype="None"
             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
             cv2.putText(imgContour,objecttype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,0,0),2)


            



img=cv2.imread("shapes.jpg")
imgContour=img.copy()
gray = img[:,:,0]
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # dimension is 2d
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)#higher value of sigma gives more..blur
#cv2.imshow("gray",imgGray)
#cv2.imshow("blur",imgBlur)
#cv2.imshow("image",img)
img = img[:,:,0] #convert 3d image to 2d
one=np.column_stack((gray,imgGray))
two=np.column_stack((one,imgBlur))
imgCanny=cv2.Canny(imgBlur,50,50)
cv2.imshow("edge",imgCanny)
getContours(imgCanny)

cv2.imshow("image",imgContour)

cv2.imshow("together",one)
cv2.waitKey(0)
cv2.destroyAllWindows()

