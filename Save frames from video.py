import numpy as np
import cv2 as cv

filename = "Background.mp4"

cap = cv.VideoCapture(filename)
if not cap.isOpened():
	print("Cannot open file")
	exit()

i = 0

while cap.isOpened():
	i += 1
	ret,frame = cap.read()

	#if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break

	cv.imshow('frame', frame)
	cv.imwrite('{}.jpeg'.format(i), frame)
	if cv.waitKey(24) == ord('q'):
		break

print("Frames:",i)

cv.waitKey(0)
cv.destroyAllWindows()