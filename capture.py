import cv2
cap = cv2.VideoCapture('E:\Video Song\Soch_Na_Sake_FULL_VIDEO_SONG__AIRLIFT__Akshay_Kumar,_Nimrat_Kaur__Arijit_Singh,_Tulsi_Kumar(1080p).mp4')

while True:
    ret,frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('CAPTURED_IMAGE',gray)
    if cv2.waitKey(9000) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()