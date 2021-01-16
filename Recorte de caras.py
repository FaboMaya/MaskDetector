import numpy as np
import cv2 as cv
import os

i = 0
carpeta = "Faces/"
files = os.listdir(carpeta)
cascade_face = cv.CascadeClassifier('cascade5/cascade.xml')

for file in files:
	img = cv.imread(carpeta + file)
	rectangles = cascade_face.detectMultiScale(img)
	for rect in rectangles:
		i += 1
		face = np.array(img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
		#cv.imshow("Face {}".format(i), face)
		cv.imwrite("Caras Recortadas/face{}.jpeg".format(i),face)
		#cv.waitKey(0)
		#cv.destroyAllWindows()
