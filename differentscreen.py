import cv2


maxScaleUp = 100
scaleFactor = 1
windowName = "Resize Image"
trackbarValue = "Scale"

#read the image
image = cv2.imread("Frame 3.png")

#Create a window to display results and  set the flag to Autosize
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("track")
cv2.resizeWindow("track",500,300)

#Callback functions
def scaleImage(args):
    #Get the scale factor from the trackbar 
    print(args)
    scaleFactor = 1+ args/100.0
    #Resize the image
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)
    
    
   


#Create trackbar and associate a callback function
cv2.createTrackbar(trackbarValue, "track", scaleFactor, maxScaleUp, scaleImage)



# Display the image
cv2.imshow(windowName, image)
c=cv2.waitKey(0) 
cv2.destroyAllWindows()