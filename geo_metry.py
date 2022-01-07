import cv2

img=cv2.imread("E:\PYTHON\PIECHART.JPG",1)

img=cv2.line(img,(0,0),(255,255),(0,0,255),5)                               #  Draw asimple one line
img=cv2.arrowedLine(img,(0,255),(200,200),(255,0,0),5)                         # Draw an arrow line

img=cv2.rectangle(img,(400,0),(520,220),(0,0,255),-1)                    #draw a rectangle

img=cv2.circle(img,(446,101),50,(0,255,0),-1)           #draw a circle .
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'opencv_project',(300,300),font,2,(128,0,128),8,cv2.LINE_8)             #putting a text in opencv using this method.
cv2.imshow("Image",img)


cv2.imwrite("GEO_LINE.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()