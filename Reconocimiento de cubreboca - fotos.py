import numpy as np
import cv2 as cv
import pickle
import os

carpeta = "Frames"
nombresArchivos = os.listdir(carpeta)
numeroArchivo = 4238
nombreArchivo = "{0}/{1}".format(carpeta,nombresArchivos[numeroArchivo])

# load the model from disk
nombreArchivoClf = "modeloSVM.sav"
clfSVM = pickle.load(open(nombreArchivoClf, 'rb'))
dataP = []

for i in range(1,6):
	cascade_face = cv.CascadeClassifier('cascade{}/cascade.xml'.format(i))
	img = cv.imread(nombreArchivo)
	rectangles = cascade_face.detectMultiScale(img)
	if len(rectangles) > 0:
		for rect in rectangles:
			img = cv.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),(255,0,0))
			if i == 5:
				face = np.array(img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
				face = cv.resize(img,(16,16))
				face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
				face = face//16
				face = face.ravel()
				print(face.shape)
				dataP.append(face)
	cv.imshow('img{}'.format(i), img)

dataP = np.array(dataP)
print(len(dataP))
if len(dataP) > 0:
	predictedSVM = clfSVM.predict(dataP[:])
	print(5,"SVM:",predictedSVM)
else:
	print("No se encontraron caras")

cv.waitKey(0)
cv.destroyAllWindows()