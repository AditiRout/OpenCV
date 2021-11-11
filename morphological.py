import cv2
import numpy as np


'''


The morphological operations we’ll be covering include:

Erosion cv2.erode(img,strcuturing element=None..means..3x3 kernel,iterations)
Dilation
Opening
Closing
Morphological gradient
Black hat
Top hat (also called “White hat”)

These image processing operations are applied to grayscale or binary
 images and are used for preprocessing for OCR algorithms, detecting barcodes, detecting license plates, and more.

More specifically, we apply morphological operations to shapes and structures inside of images.


We can use morphological operations to increase the size of objects in images as well as decrease them.
 We can also utilize morphological operations to close gaps between objects as well as open them.
 Morphological operations “probe” an image with a structuring element. This structuring element defines the neighborhood to be examined around each pixel. 
 And based on the given operation and the size of the structuring element we are able to adjust our output image.


'''


# structuring element as a type of kernel or mask.A structuring element is a matrix that identifies the pixel in the image being 
# processed and defines the neighborhood used in the processing of each pixel. 
#The cv2.getStructuringElement function requires two arguments: the first is the type of structuring element we want, 
# and the second is the size of the structuring element
#cv2.MORPH_RECT to indicate that we want a rectangular structuring element. But you could also pass in a value of cv2.MORPH_CROSS to get a cross shape structuring element (a cross is like a 4-neighborhood structuring element, but can be of any size),
#  or cv2.MORPH_ELLIPSE to get a circular structuring element.
# of kernels sizes that will be applied to the image
image=cv2.imread("crop.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels sizes
for kernelSize in kernelSizes:
	# construct a rectangular kernel from the current size and then
	# apply an "opening" operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)#get our own..structuring element
    #cv2.morphologyEx function. This function is abstract in a sense — it allows us to pass in whichever morphological operation we want, followed by our kernel/structuring element.

#The first required argument of cv2.morphologyEx is the image we want to apply the morphological operation to.
#  The second argument is the actual type of morphological operation — in this case, it’s an opening operation.
#  The last required argument is the kernel/structuring element that we are using.
#an opening operation allows us to remove small blobs in an image.
#closing operation is to connect componenets together and close holes inside of objects
# morphological gradient is the difference between a dilation and erosion.
# It gives us a boundary. It is useful for determining the outline of a particular object of an image:
#A top hat operation is used to reveal bright regions of an image on dark backgrounds.
#
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(
		kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)