import numpy as np
import cv2 as cv

filename = "vt_1.mp4"

cap = cv.VideoCapture(filename)
if not cap.isOpened():
	print("Cannot open file")
	exit()

cascade_face = cv.CascadeClassifier('cascade5/cascade.xml')

while cap.isOpened():
	ret,frame = cap.read()

	
	rectangles = cascade_face.detectMultiScale(frame)
	for rect in rectangles:
		frame = cv.rectangle(frame,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(0,255,0))

	#if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break

	cv.imshow('frame', frame)
	if cv.waitKey(1) == ord('q'):
		break

cv.waitKey(0)
cv.destroyAllWindows()