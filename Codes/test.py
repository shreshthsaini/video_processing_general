import os 
import numpy as np 
import cv2 


img = cv2.imread("/Users/shreshthsaini/Desktop/DeltaE_8bit_gamma2.2.tif")
print(img.shape)

def filtering(img,kernel):
    operated = cv2.filter2D(img, -1, kernel)
    return operated


#mean filtering 
kernel = np.ones((20,20),np.float32)/(20*20)

#cv2.imshow('mean_blur', filtering(img, kernel))
cv2.imwrite('mean_blur.png', filtering(img, kernel))

