import cv2

img=cv2.imread("E:\PYTHON\Line Appearance.JPG",1)  #0=grey scale image

cv2.imshow("Line Appearance",img)
cv2.waitKey(6000)  #if you write here as 0, your image will be displayed at infinite time.
cv2.destroyAllWindows()
cv2.imwrite("GREY_LINE_APPERANCE.png",img)