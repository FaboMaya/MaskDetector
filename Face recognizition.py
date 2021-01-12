import numpy as np
import cv2 as cv

filename = "People/1609964130.8983057.jpg"

img1 = cv.imread(filename)
cascade_face1 = cv.CascadeClassifier('cascade1/cascade.xml')
rectangles1 = cascade_face1.detectMultiScale(img1)
for rect in rectangles1:
	img1 = cv.rectangle(img1,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(255,0,0))
print(len(rectangles1))
cv.imshow('img1', img1)

img5 = cv.imread(filename)
cascade_face4 = cv.CascadeClassifier('cascade5/cascade.xml')
rectangles5 = cascade_face4.detectMultiScale(img5)
for rect in rectangles5:
	img5 = cv.rectangle(img5,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(0,255,0))
print(len(rectangles5))
cv.imshow('img5', img5)

cv.waitKey(0)
cv.destroyAllWindows()