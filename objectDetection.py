import cv2 
import numpy as np
from datetime import datetime
firstImage=None 

capture=cv2.VideoCapture(0)

while True:
    check,frame=capture.read()
    if firstImage is None:
        firstImage=frame
    difference=cv2.subtract(firstImage,frame)
    is_all_zeroes=np.all((difference==0))
    if is_all_zeroes:
        print("No image detected."+str(datetime.now()))
    else:
        print("Image Detected "+str(datetime.now()))
    cv2.imshow("Object Detection:",frame)
    cv2.imshow("Object Detection Diffrence:",difference)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break


    

    

