import cv2 
import numpy as np

# read the image 
image = cv2.imread('download_01.jpg')
# get the width and height of the image
height, width = image.shape[:2]
tx=width/4
ty=height/4
transate_mat=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)
newimag=cv2.warpAffine(src=image,M=transate_mat,dsize=(width,height))
# display the original and the Translated images
cv2.imshow('Translated image', newimag)
cv2.imshow('Original image', image)
cv2.waitKey(0)
# save the translated image to disk
cv2.imwrite('translated_image.jpg', newimag)
