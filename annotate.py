import cv2 
import numpy as np

imag=cv2.imread("download_01.jpg")
cv2.imshow("original",imag);
cv2.waitKey(0)
#Make copy of the image
imageLine = imag.copy()
# Draw the image from point A to B
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)

circle_center = (415,190)
# define the radius of the circle
radius =100
#  Draw a circle using the circle() Function
cv2.circle(imageLine, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA) 
# Display the result
cv2.imshow("Image Circle",imageLine)
cv2.waitKey(0)

circle_center = (415,190)
# define the radius of the circle
radius =100
# draw the filled circle on input image
cv2.circle(imageLine, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# display the output image 
cv2.imshow('Image with Filled Circle',imageLine)
cv2.waitKey(0)
ellipse_center = (415,190)
# define the axis point(mention the lengths of x and y)
axis1 = (200,50)
# draw the Incomplete/Open ellipse, just a outline
cv2.ellipse(imageLine, ellipse_center, axis1, 0, 180, 360, (255, 0, 0), thickness=3)
# if you want to draw a Filled ellipse, use this line of code
cv2.ellipse(imageLine, ellipse_center, axis1, 0, 0, 180, (0, 0, 255), thickness=-2)
# display the output
cv2.imshow('halfEllipse',imageLine)
cv2.waitKey(0)

text="good morning"
org=(300,300)
cv2.putText(imageLine,text,org,fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1.5,color=(255,0,255))
cv2.imshow("final",imageLine)
cv2.waitKey(0)
cv2.destroyALLWindows()


# FONT_HERSHEY_SIMPLEX        = 0,
#  FONT_HERSHEY_PLAIN          = 1,
 # FONT_HERSHEY_DUPLEX         = 2,
 # FONT_HERSHEY_COMPLEX        = 3,
#  FONT_HERSHEY_TRIPLEX        = 4,
#  FONT_HERSHEY_COMPLEX_SMALL  = 5,
#  FONT_HERSHEY_SCRIPT_SIMPLEX = 6,
#  FONT_HERSHEY_SCRIPT_COMPLEX = 7,
 # FONT_ITALIC                 = 16
