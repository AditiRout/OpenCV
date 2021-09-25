import cv2 as cv
import numpy as np
video= cv.VideoCapture("Project Name.mp4")#sameas imread
if(video.isOpened()==False):
    print("error while opening")


#to get fps and frame count and width by using get function

else:
    fps=video.get(cv.CAP_PROP_FPS)
    print("Frame Rate : ",fps,"frames per second")
    frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
    print("Frame count : ", frame_count)
    width=video.get(cv.CAP_PROP_FRAME_WIDTH)
    print("width:",width)
    
    


while True:#can write(while(video.isOpened())
    ret,frame=video.read()#to read and get two values one in bool other is the frame
    if ret==True:
        #gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #cv.imshow("Frame",gray)
        cv.imshow("FRAME",frame)
        k=cv.waitKey(100)
        if k==ord('q'):
           break
    else:
        break
video.release()
cv.destroyAllWindows()
