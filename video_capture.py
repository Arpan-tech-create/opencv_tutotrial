import cv2
import datetime

cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1500)  #3 for width of frame
cap.set(4,1000)     #4 for height of frame

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):

    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX

        text='width :' + str(cap.get(3))   +   'Height :' + str(cap.get(4))
        date1=str(datetime.datetime.now())
        frame=cv2.putText(frame,date1,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

    if cv2.waitKey(0) & 0xFF ==ord('q'):

        break
    else:
        break
cap.release()
cv2.destroyAllWindows()