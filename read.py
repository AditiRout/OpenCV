import cv2 as cv
import sys

img_c=cv.imread("59561.jpg",cv.IMREAD_COLOR)#to read image in same color
img_u=cv.imread("59561.jpg",cv.IMREAD_UNCHANGED)#same color
img_g=cv.imread("59561.jpg",cv.IMREAD_GRAYSCALE)#b&w


if img_c is None:
    sys.exit("Could not read")

#display tabs
cv.imshow("Chemis",img_c)
cv.imshow("Chemistry",img_g)
cv.imshow("Chem",img_u)

#waiting for user for the key press to close window
k=cv.waitKey(0)
cv.destroyWindow("Chemis")
cv.destroyAllWindows()
if k==ord("s"):  #s key
    cv.imwrite("59561ag.jpg",img_g)#to save image with that filename


