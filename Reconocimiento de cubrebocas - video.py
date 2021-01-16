import numpy as np
import cv2 as cv
import pickle

filename = "vt_1.mp4"

# load the model from disk
nombreArchivoClf = "modeloMLP.sav"
clfSVM = pickle.load(open(nombreArchivoClf, 'rb'))
dataP = []

cap = cv.VideoCapture(filename)
if not cap.isOpened():
	print("Cannot open file")
	exit()

cascade_face = cv.CascadeClassifier('cascade5/cascade.xml')

while cap.isOpened():
	ret,frame = cap.read()
	
	rectangles = cascade_face.detectMultiScale(frame)
	
	if len(rectangles) > 0:
		for rect in rectangles:
			face = np.array(frame[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
			face = cv.resize(face,(16,16))
			face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
			face = face//16
			face = face.ravel()
			#print(face.shape)
			dataP.append(face)
			predictedSVM = clfSVM.predict([face])
			#print(5,"SVM:",predictedSVM)
			color = None
			if predictedSVM == ["Cubreboca"]:
				color = (0,255,0)
			elif predictedSVM == ["Otros"]:
				color = (255,0,0)
			else:
				color = (0,0,255)
			frame = cv.rectangle(frame,(rect[0],rect[1]),(rect[0]+rect[2],rect[1]+rect[3]),color,3)

	#if frame is read correctly ret is True
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break

	cv.imshow('frame', frame)
	if cv.waitKey(1) == ord('q'):
		break
"""
dataP = np.array(dataP)
print(len(dataP))
if len(dataP) > 0:
	predictedSVM = clfSVM.predict(dataP[:])
	print(5,"SVM:",predictedSVM)
else:
	print("No se encontraron caras")
"""
cv.destroyAllWindows()
