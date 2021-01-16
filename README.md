# MaskDetector
Descripción de uso
En un mismo directorio se deben ubicar los siguientes archivos:
1.	“Reconocimiento de cubreboca - fotos.py”.
2.	“Reconocimiento de cubreboca - video.py”.
3.	“modeloMLP.sav”.
4.	Carpeta “cascade1” (descomprimir “cascade1.zip”).
5.	Carpeta “cascade2” (descomprimir “cascade2.zip”).
6.	Carpeta “cascade3” (descomprimir “cascade3.zip”).
7.	Carpeta “cascade4” (descomprimir “cascade4.zip”).
8.	Carpeta “cascade5” (descomprimir “cascade5.zip”).
9.	Carpeta “Samples” (descomprimir “Samples.zip”).
10.	“vt1.mp4”.
https://drive.google.com/file/d/1IbGwjuZTNklizy7KTuSXaUpaJ7mkZTDC/view?usp=sharing
11.	“vt2.mp4”. 
https://drive.google.com/file/d/15hqWH_NTjr-33lWhrE1f4ruNDCmDP1Fx/view?usp=sharing
12.	“vt3.mp4”.
https://drive.google.com/file/d/1rh_h7dQ-J6p-XUVoPcVgjjxQd9ylK0Wp/view?usp=sharing
13.	“vt4.mp4”. 
https://drive.google.com/file/d/1RyWWtJia5R347M8HkV275gzOUM5nr54a/view?usp=sharing

Imágenes
1.	Correr el archivo “Reconocimiento de cubreboca - fotos.py”. 
2.	Se desplegarán 1 ventana de Python y 1 ventana de OpenCV.
3.	En la ventana de OpenCV, se mostrara la imagen, con las caras resaltadas por un marco rectangular de color verde, rojo o azul, que corresponde a “cubreboca”, “sin cubreboca” y “no es cara” respectivamente.
4.	Para terminar el programar hay que cerrar la ventana de Python con el botón de “Cerrar”.
Se puede probar usar otra foto al cambiar el valor de la variable “numeroArchivo”, ubicada en la línea 8 del código del programa, por cualquier número entre 0 y 19.
Se puede cambiar el clasificador en cascada al cambiar el valor de la variable “cascada”, ubicada en la línea 12 del código del programa, por cualquier número entre 1 y 5. 1 corresponde a un clasificador de 10 etapas, 2 a un clasificador de 20 etapas, 3 a uno de 30, 4 a 40 y 5 a uno de 50 etapas.

Videos
1.	Correr el archivo “Reconocimiento de cubreboca - video.py”. 
2.	Se desplegarán 1 ventana de Python y 1 ventana de OpenCV.
3.	En la ventana de OpenCV, se mostrara el video, con las caras resaltadas por un marco rectangular de color verde, rojo o azul, que corresponde a “cubreboca”, “sin cubreboca” y “no es cara” respectivamente.
4.	Para terminar el programar hay que cerrar la ventana de Python con el botón de “Cerrar”.
Se puede probar usar otro video al cambiar el valor de la variable “numeroArchivo”, ubicada en la línea 12 del código del programa, por cualquier número entre 0 y 4.
Se puede cambiar el clasificador en cascada al cambiar el valor de la variable “cascada”, ubicado en la línea 16 del código del programa, por cualquier número entre 1 y 5. 1 corresponde a un clasificador de 10 etapas, 2 a un clasificador de 20 etapas, 3 a uno de 30, 4 a 40 y 5 a uno de 50 etapas.
