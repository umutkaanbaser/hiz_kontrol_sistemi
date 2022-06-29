import os
import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture("video.mp4")


negSayisi=0
pozSayisi=0
while True:
    ret,frame = cap.read()
    if ret:

        cv2.imshow("frame",frame)
        key = cv2.waitKey(10)
        if(key==ord("q")):
            break
        elif key == ord("n"):
            cv2.imwrite(f"n/neg{negSayisi}.jpg",frame) #neg1.jpg
            negSayisi+=1
        elif key == ord("p"):
            cv2.imwrite(f"p/poz{pozSayisi}.jpg",frame)
            pozSayisi+=1
    else:
        break

cap.release()
