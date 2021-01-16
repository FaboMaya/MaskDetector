from sklearn.neural_network import MLPClassifier
import numpy as np
import cv2 as cv
import pickle
import os

carpeta = "Caras Recortadas"
list_ctg = os.listdir(carpeta)

list_ctg0 = os.listdir("{0}/{1}".format(carpeta, list_ctg[0]))
list_ctg1 = os.listdir("{0}/{1}".format(carpeta, list_ctg[1]))
list_ctg2 = os.listdir("{0}/{1}".format(carpeta, list_ctg[2]))

filenames = []
filenames.append(list_ctg0)
filenames.append(list_ctg1)
filenames.append(list_ctg2)

len_ctgs = np.array([len(list_ctg0), len(list_ctg1), len(list_ctg2)])

print("Categorías: \n 1. {0} ({3}) \n 2. {1} ({4}) \n 3. {2} ({5})".format(list_ctg[0],list_ctg[1],list_ctg[2],
	len(list_ctg0),len(list_ctg1),len(list_ctg2)))

minimo = min(len_ctgs)
steps = len_ctgs//minimo
imgsCtgs = []

print(minimo)

conteo = 0

for j in range(len(list_ctg)):
	lista_img = []
	for i in range(0,len_ctgs[j],steps[j]):
		img = cv.imread("{0}/{1}/{2}".format(carpeta,list_ctg[j],filenames[j][i]),0)
		img2 = cv.resize(img,(16,16))
		img2 = img2//16
		img2 = img2.ravel()
		lista_img.append(img2)
		conteo += 1
		if conteo >= minimo:
			conteo = 0
			break
	imgsCtgs.append(lista_img)

imgsCtgs = np.array(imgsCtgs)
print(imgsCtgs.shape)

data = []
target = []
for j in range(len(list_ctg)):
	for i in range(35):
		target.append(list_ctg[j])
	for img in imgsCtgs[j]:
		data.append(img)
data = np.array(data)
target = np.array(target)

dataP = []
for j in range(len(list_ctg)):
	for i in [1, 10 , 20]:
		img = cv.imread("{0}/{1}/{2}".format(carpeta,list_ctg[j],filenames[j][i]),0)
		img2 = cv.resize(img,(16,16))
		img2 = img2//16
		img2 = img2.ravel()
		dataP.append(img2)
dataP = np.array(dataP)

print(data.shape,target.shape)

valoresReales = [list_ctg[0],list_ctg[0],list_ctg[0],list_ctg[1],list_ctg[1],list_ctg[1],
list_ctg[2],list_ctg[2],list_ctg[2]]

mejor = [0,9,None] # [Layers,errores,clasificador]
for i in range(1,300):
	clfMLP = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(i,),random_state=1)
	clfMLP.fit(data[:], target[:])
	predictedMLP = clfMLP.predict(dataP[:])
	#print("MLP:",predictedMLP)
	erroresMLP = 0
	for j in range(len(predictedMLP)):
		if predictedMLP[j] != valoresReales[j]:
			erroresMLP += 1
	if mejor[1] > erroresMLP:
		mejor = [i,erroresMLP,clfMLP]
		if mejor[1] == 0:
			break
	print(i,erroresMLP)

print(mejor)

# save the model to disk
filename = 'modeloMLP.sav'
pickle.dump(mejor[2], open(filename, 'wb'))

"""
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
"""