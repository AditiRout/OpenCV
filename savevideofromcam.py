
# importing libraries
import cv2
import numpy as np
   
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)   
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video  file")
framewidth=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameh=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size=(framewidth,frameh)
result=cv2.VideoWriter("save.avi",cv2.VideoWriter_fourcc('M','J','P','G'),100,size)
   
# Read until video is completed
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    result.write(frame)
   
    # Display the resulting frame
    cv2.imshow('Frame', frame)
   
    # Press Q on keyboard to  exit waitkeyvalue helps to manipulate speed
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
result.release()
   
# Closes all the frames
cv2.destroyAllWindows()
