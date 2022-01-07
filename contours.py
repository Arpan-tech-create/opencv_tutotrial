import numpy as np
import cv2

img=cv2.imread("E:\PYTHON\OpenCV_Logo.JPG")  

imgG=cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(imgG,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of Contours :" +str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,0,128),5)

cv2.drawContours(imgG,contours,-1,(0,0,128),5)

cv2.imshow("ORIGINAL_IMAGE",img)
cv2.imshow("GRAY_SCALE_IMG",imgG)
cv2.waitKey(0)  #if you write here as 0, your image will be displayed at infinite time.
cv2.destroyAllWindows()
