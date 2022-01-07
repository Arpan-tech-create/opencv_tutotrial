import cv2
img=cv2.imread("E:\PYTHON\Annotation 2020-11-05 192114.png",1) #for reading image we used imread method.
                                                                #1=flag-value 1=loads a color image
                                                                            #0=loads a grey scale image
                                                                            #-1=loads image as such including alpha channel.
cv2.imshow("BAR_Chart",img) # for giving title of this image.
cv2.waitKey(3000) #how much time image can be displayed. here 3ms=3000s
cv2.destroyAllWindows()
cv2.imwrite("BAR_CHART.png",img)