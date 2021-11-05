# Import packages
import cv2

# Lists to store the bounding box coordinates
top_left_corner=[]
bottom_right_corner=[]

# function which will be called on mouse input
#Whenever the user interacts with the mouse, while it is over the image being displayed: The mouse event type and event flags are recorded, along with the mouse x and y coordinates. These are then passed to the function for processing. *userdata is an optional argument that can provide further inputs to the callback function (we will not require it in this example though).
def drawRectangle(action, x, y, flags, *userdata):
  # Referencing global variables 
  global top_left_corner, bottom_right_corner
  # Mark the top left corner when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]    
    # Draw the rectangle
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Window",image)

# Read Images
image = cv2.imread("shruti.png")
# Make a temporary image, will be useful to clear the drawing
temp = image.copy()
# Create a named window
cv2.namedWindow("Window")
# highgui function called when mouse events occur,
#cv2.setMouseCallback(winname, onMouse, userdata)
# winname: Name of the window
#onMouse: Callback function for mouse events
#userdata: Optional argument passed to the callback
cv2.setMouseCallback("Window", drawRectangle)

k=0
# Close the window when key q is pressed
while k!=113:
  # Display the image
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  # If c is pressed, clear the window, using the dummy image
  if (k == 99):
    image= temp.copy()
    cv2.imshow("Window", image)

cv2.destroyAllWindows()