from matplotlib import pyplot as plt
import cv2


photo=cv2.imread("59561.jpg")
img=plt.imshow(photo)
plt.show()

z=plt.imshow(photo[::-1])#reverse image
plt.show()

y=plt.imshow(photo[:,::-1])
plt.show()#reverse image horizontally

k=plt.imshow(photo[50:150,150:280])
plt.show()#crop image

h=plt.imshow(photo[::2,::2])
plt.show()



