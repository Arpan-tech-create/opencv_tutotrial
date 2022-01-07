import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
cap=cv2.VideoCapture(5000)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x, ',',y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+','+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(0,255,0),2)
        cv2.imshow("IMAGE",img)
img=np.zeros((512,512,3),np.uint0)
cv2.imshow("IMAGE",img)
cv2.setMouseCallback("IMAGE",click_event)

cv2.waitKey(6000)
cv2.destroyAllWindows()