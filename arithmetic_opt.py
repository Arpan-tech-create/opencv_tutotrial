import cv2

img=cv2.imread("E:\PYTHON\PIECHART.JPG")

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
print(img.shape)           #shape represents the rows,columns,channels.
print(img.size)            # size of the image or (number of pixels)
print(img.dtype)            # define the datatype.

cv2.imshow("PIECHART",img)
cv2.waitKey(0)

cv2.destroyAllWindows()