import numpy as np
import cv2 as cv

filename = "People/1610230676.705771.jpg"
cascade_face = cv.CascadeClassifier('cascade{}/cascade.xml'.format(i))

for i in range(1,6):
	img = cv.imread(filename)
	rectangles = cascade_face.detectMultiScale(img)
	for rect in rectangles:
		img = cv.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(255,0,0))
	print(i,":",len(rectangles))
	cv.imshow('img{}'.format(i), img)

cv.waitKey(0)
cv.destroyAllWindows()