import cv2 as cv
#program to resize an image according to our own requirements
image=cv.imread("download_01.jpg")
cv.imshow("original",image)
x=300
y=400
si=(x,y)
si2=(x,100)
h,w,c=image.shape
print("the original image has height,width:",h,w)
print("press key s to get a resized image")
m=cv.waitKey(0)
# Display images and press any key to check next image



if m==ord('s'):
    
    print("enter the scaling factor:")
    scale=float(input())
    newi=cv.resize(image,None,fx=scale,fy=scale,interpolation=cv.INTER_AREA)
    cv.imshow("newone",newi)
    cv.waitKey()
    newi2=cv.resize(image,None,fx=scale,fy=scale,interpolation=cv.INTER_CUBIC)
    cv.imshow("newone2",newi2)
    cv.waitKey()
    newi3=cv.resize(image,None,fx=scale,fy=scale,interpolation=cv.INTER_LINEAR)
    cv.imshow("newone3",newi3)
    cv.waitKey()
    # Display images and press any key to check next image
    scaledown=cv.resize(image,si,interpolation=cv.INTER_LINEAR)
    cv.imshow('Resized Down by defining scaling factor', scaledown)
    cv.waitKey()
    scaleup=cv.resize(image,si2,interpolation=cv.INTER_LINEAR)
    cv.imshow('Resized Up image by defining scaling factor',scaleup)
    cv.waitKey()
    newi4=cv.resize(image,None,fx=scale,fy=scale,interpolation=cv.INTER_NEAREST)
    cv.imshow("newone4",newi4)
    k=cv.waitKey(0)
    cv.destroyAllWindows()
    if k==ord('q'):
        cv.imwrite("newone1.jpg",newi)
    
    



