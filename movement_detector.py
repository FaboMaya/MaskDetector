import cv2 as cv
import numpy as np
import time

cap = cv.VideoCapture(0)

if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

ret, last_frame = cap.read()
last_frame = cv.cvtColor(last_frame,cv.COLOR_BGR2GRAY)
i = 0

while True:
	ret, frame = cap.read()
	frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
	if frame is None:
		print('--(!) No captured frame -- Break!')
		break

	#condition = np.allclose(frame_gray, last_frame, rtol=1.5, atol=40)
	hist = cv.calcHist([frame_gray],[0],None,[256],[0,256])
	last_hist = cv.calcHist([last_frame],[0],None,[256],[0,256])
	comparison = cv.compareHist(hist,last_hist,5)
	condition = comparison < 1000

	if condition:
		print(condition,"same")
	else:
		print(condition,"different")
		cv.imwrite("frames/{}.jpg".format(time.time()),frame)
	
	
	last_frame = frame_gray[:]
	cv.imshow("Frame",frame)

	if cv.waitKey(250) == 27:
	    break

cv.destroyAllWindows()