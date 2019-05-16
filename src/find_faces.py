import cv2 as cv
import numpy as np

img1 = cv.imread('ucb1.jpg')
img2 = cv.imread('ucb2.jpg')

img1 = cv.resize(img1, (0,0), fx=0.25, fy=0.25)
img2 = cv.resize(img2, (0,0), fx=0.25, fy=0.25)

img_gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img_gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(img_gray1, scaleFactor=1.1, minNeighbors=5)
faces2 = face_cascade.detectMultiScale(img_gray2, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in faces:
    cv.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)

for (x,y,w,h) in faces2:
    cv.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('ucb1', img1)
cv.imshow('ucb2', img2)
cv.waitKey()
cv.destroyAllWindows()

