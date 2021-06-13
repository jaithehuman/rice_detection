from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def vidcap():
	print("starting webcam")
	vid = cv2.VideoCapture(0)
	x,y,h,w = 45,5,440,465
	i = 0
	print("webcam ready")

	while(True):

		ret, frame = vid.read()
		img = frame[y:y+h,x:x+w]

		# cv2.imshow('res', img)

		cv2.imwrite(str(i)+'.jpg',img) #cap

		print("captured!")

		if i == 10:
			print("done")
			cv2.destroyAllWindows()
			break

		i += 1
		
	vid.release()


def count():
	x = [0]*10
	for i in range(10):
		print(i)
		image = cv2.imread(str(i)+'.jpg')
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		edged = cv2.Canny(gray, 50, 100)
		edged = cv2.dilate(edged, None, iterations=1)
		edged = cv2.erode(edged, None, iterations=1)

		cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		(cnts, _) = contours.sort_contours(cnts)


		rice = int(str(len(cnts))) - 1
		x[i] = rice
		print("image_"+str(i)+"_count:", rice)
		print()

		cv2.drawContours(image,cnts,-1,(0,255,0),3)
		cv2.imshow("exp",image)
		cv2.imshow("edge",edged)
		cv2.imshow("gray",gray)
		cv2.waitKey(0)
		cv2.destroyAllWindows
	print(x)
	print("Highest rice count:"+str(max(x)))
	plt.hist(x)
	plt.show()


def start():
	#open webcam
	print("starting webcam")
	vid = cv2.VideoCapture(0)
	x,y,h,w = 45,5,440,465
	i = 0
	print("webcam ready")

	# capture before
	# ret, frame = vid.read()
	# img = frame[y:y+h,x:x+w]
	# cv2.imwrite(str(i)+'.jpg',img)
	# print(i)
	# i += 1

	#run arduino
	num = 'H'
	time.sleep(1)
	arduino.write(bytes(num, 'utf-8'))
	print("start arduino")
	time.sleep(1)
	#capture frame
	while(True):

		ret, frame = vid.read()
		img = frame[y:y+h,x:x+w]

		if i == 10:
			print("done")
			cv2.destroyAllWindows()
			break

		cv2.imwrite(str(i)+'.jpg',img) #cap
		print(i)
		i += 1
		time.sleep(2.1)
		
	vid.release()



if __name__ == '__main__':
	start()


