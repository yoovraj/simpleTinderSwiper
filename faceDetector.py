#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FACIAL RECOGNITION
# OPENCV and HAAR CASCADES


import cv2
import numpy as np
import serial
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(1)
s = serial.Serial(port='/dev/cu.usbmodem1411',baudrate=9600)   # open serial port that Arduino is using


# if face is detected (<0) swipe right, if 0 (no face) swipe left

while True:
    time.sleep(2)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    if (len(faces)) == 0:
        s.write(b'l')
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # print(len(eyes))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    for (x, y, w, h) in faces:
        if w > 0 :                 #--- Set the flag True if w>0 (i.e, if face is detected)
            face_found = True
        else:
            face_found = False
        if face_found == True:
            s.write(b'r')
            time.sleep(2)
        if face_found == False:
            s.write(b'l')
            time.sleep(2)



    cv2.imshow("img",img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows






'''

cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)  #--- highlight the face
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'name',(0,130), font, 1, (200,255,155)) #---write the text
cv2.imshow('Face having name', image)

'''
