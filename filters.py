import cv2
import numpy as np

img=cv2.imread("download_01.jpg")
kernal=np.array([[1,1,1],[1,1,1],[1,1,1]])#max resultss if 5x5 matrix
kernal=kernal/sum(kernal)

img=cv2.filter2D(img,-1,kernal)
cv2.imshow("lowpassfilter",img)
cv2.waitKey(0)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
# loop over the kernel sizes
for (kX, kY) in kernelSizes:
	# apply an "average" blur to the image using the current kernel
	# size
	blurred = cv2.blur(img, (kX, kY))
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)
cv2.destroyAllWindows()
for (kX, kY) in kernelSizes:
	# apply a "Gaussian" blur to the image
	blurred = cv2.GaussianBlur(img, (kX, kY), 0)
	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

cv2.destroyAllWindows()
for k in (3, 5,9, 15):
    #oil painting effect here
	# apply a "median" blur to the image
	blurred = cv2.medianBlur(img, k)
	cv2.imshow("Median {}".format(k), blurred)
	cv2.waitKey(0)

cv2.destroyAllWindows()
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39),(11,41,7)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	blurred = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
	# show the output image and associated parameters
	title = "Blurred d={}, sc={}, ss={}".format(
		diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)
