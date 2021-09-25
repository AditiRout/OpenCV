import cv2 as cv
#program to resize an image according to our own requirements
image=cv.imread("doodle.jpg")
cv.imshow("original",image)
h,w,c=image.shape
print("the original image has height,width:",h,w)
print("press key s to get a resized image")
m=cv.waitKey(0)

if m==ord('s'):
    
    print("enter the scaling factor:")
    scale=float(input())
    newi=cv.resize(image,None,fx=scale,fy=scale,interpolation=cv.INTER_LINEAR)
    cv.imshow("newone",newi)
    k=cv.waitKey(0)
    cv.destroyAllWindows()
    if k==ord('q'):
        cv.imwrite("newone1.jpg",newi)
    
    





