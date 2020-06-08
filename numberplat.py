import cv2
import numpy as numpy
frameWidth = 640
frameheight = 480
color = (255,0,255)
count = 0
numberp = cv2.CascadeClassifier("D:/windows_10/opencv/sources/data/haarcascades/haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameheight)
cap.set(10,150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplate = numberp.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in numberplate:
        area = w*h
        if area>500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("img",imgRoi)

    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("E:/save/numberplate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"scanned",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("result",img)
        cv2.waitKey(500)
        count +=1