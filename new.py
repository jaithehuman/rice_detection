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
import os
import sys
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def count(path):
	print("start counting")
	total = [0]*10
	f = open(path+"result.txt","w+")
	f.write("test"+str(path[-2]))
	# for i in range(10):
	# 	image = cv2.imread(path +str(i)+'.jpg')
	# 	# image = cv2.imread("./test3/9.jpg")
	# 	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	# 	lower_white = np.array([0,0,180], dtype=np.uint8)
	# 	upper_white = np.array([180,50,255], dtype=np.uint8)

	# 	mask = cv2.inRange(hsv,lower_white,upper_white)
	# 	res = cv2.bitwise_and(image,image,mask=mask)

	# 	gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

	# 	cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
	# 				cv2.CHAIN_APPROX_SIMPLE)
	# 	cnts = imutils.grab_contours(cnts)
	# 	(cnts, _) = contours.sort_contours(cnts)


	# 	cv2.drawContours(image,cnts,-1,(0,255,0),2)

	# 	rice = int(str(len(cnts)))
	# 	x[i] = str(rice)
	# 	f.write("\nimage_"+str(i))
	# 	f.write("\ncount:"+str(rice))
	# 	f.write("\n")
	# 	print("image_" + str(i))
	# 	print("count:"+ str(rice))
	# 	print()
	# 	cv2.imshow("ori",image)
	# 	cv2.imshow("mask",mask)
	# 	cv2.imshow("gray",gray)
	# 	cv2.waitKey(0)
	# 	cv2.destroyAllWindows
	for i in range(10):
		I = cv2.imread(path +str(i)+'.jpg', 0)
		h,w = I.shape[:2]
		diff = (3,3,3)
		mask = np.zeros((h+2,w+2),np.uint8)
		cv2.floodFill(I,mask,(0,0), (255,255,255),diff,diff)
		T,I = cv2.threshold(I,180,255,cv2.THRESH_BINARY)
		# I = cv2.medianBlur(I, 7)

		totalrice = 0
		oldlinecount = 0
		for y in range(0, h):
			oldc = 0
			linecount = 0
			start = 0   
			for x in range(0, w):
				c = I[y,x] < 128;
				if c == 1 and oldc == 0:
					start = x
				if c == 0 and oldc == 1 and (x - start) > 10:
					linecount += 1
				oldc = c
			if oldlinecount != linecount:
				if linecount < oldlinecount:
					totalrice += oldlinecount - linecount
				oldlinecount = linecount
		f.write("\nimage_"+str(i))
		f.write("\ncount:"+str(totalrice))
		f.write("\n")
		total[i] = str(totalrice)
		print(totalrice)
		

	
	f.write("\nHighest rice count:"+str(max(total)))
	f.close()
	print(total)
	print("Highest rice count:"+str(max(total)))
	plt.hist(total)
	plt.show()


def start():
	path = create_dir()
	print("Created new path:",path)
	#open webcam
	print("starting webcam")
	vid = cv2.VideoCapture(0)
	x,y,h,w = 45,5,440,465
	i = 0
	
	while(True):
		ret, frame = vid.read()
		img = frame[y:y+h,x:x+w]
		cv2.imshow("calibrate",img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.imwrite(path+str(i)+'.jpg',img)
			print(i)
			i += 1
			cv2.destroyAllWindows()
			break
	print("webcam ready")

	

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
			break

		cv2.imwrite(path +str(i)+'.jpg',img) #cap
		print(i)
		i += 1
		time.sleep(2.1)
		
	vid.release()
	count(path)

def create_dir():
	path=os.path.dirname("./exp/")

	latest = os.listdir(path)
	if latest == []:
		latest_dir = "exp/test0/"
	
	else:
		latest_dir = "exp/test"+str(int(max(latest)[-1])+1)+"/"
	os.mkdir(latest_dir)
	# print(latest_dir)
	return latest_dir

if __name__ == '__main__':
	start()


