import numpy as np
import cv2 as cv
import pickle
import os

carpeta = "Samples"
nombresArchivos = os.listdir(carpeta)
numeroArchivo = 1 	# Usar cualquier número entre 0 y 19 para cambiar de imagen
nombreArchivo = "{0}/{1}".format(carpeta,nombresArchivos[numeroArchivo])

# Para cambiar el numero de etapas del clasificador en cascada al cambiar este número por cualquiera entre 1 y 5.
cascada = 5 
"""
 1 = 10 etapas
 2 = 20 etapas
 3 = 30 etapas
 4 = 40 etapas
 5 = 50 etapas
"""

# load the model from disk
nombreArchivoClf = "modeloMLP.sav"
clfMLP = pickle.load(open(nombreArchivoClf, 'rb'))
dataP = []

cascade_face = cv.CascadeClassifier('cascade{}/cascade.xml'.format(cascada))
img = cv.imread(nombreArchivo)
rectangles = cascade_face.detectMultiScale(img)
	
if len(rectangles) > 0:
	for rect in rectangles:
		face = np.array(img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
		face = cv.resize(face,(16,16))
		face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
		face = face//16
		face = face.ravel()
		#print(face.shape)
		dataP.append(face)
		predictedMLP = clfMLP.predict([face])
		#print(5,"MLP:",predictedMLP)
		color = None
		if predictedMLP == ["Cubreboca"]:
			color = (0,255,0)
		elif predictedMLP == ["Otros"]:
			color = (255,0,0)
		else:
			color = (0,0,255)
		img = cv.rectangle(img,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),color,3)
cv.imshow('img', img)

dataP = np.array(dataP)
#print(len(dataP))
if len(dataP) > 0:
	predictedMLP = clfMLP.predict(dataP[:])
	print(predictedMLP)
else:
	print("No se encontraron caras")

cv.waitKey(0)
cv.destroyAllWindows()
