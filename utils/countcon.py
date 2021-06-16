from imutils import contours
import imutils
import cv2
import numpy as np
from numpy.core.fromnumeric import reshape
import matplotlib.pyplot as plt


x = [0]*10

for i in range(10):
	image = cv2.imread(str(i)+'.jpg')
	# image = cv2.imread("./test3/9.jpg")
	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	lower_white = np.array([0,0,180], dtype=np.uint8)
	upper_white = np.array([180,50,255], dtype=np.uint8)

	mask = cv2.inRange(hsv,lower_white,upper_white)
	res = cv2.bitwise_and(image,image,mask=mask)

	gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

	cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	(cnts, _) = contours.sort_contours(cnts)


	cv2.drawContours(image,cnts,-1,(0,255,0),2)

	rice = int(str(len(cnts)))
	x[i] = str(rice)
	print("image_" + str(i))
	print("count:"+ str(rice))
	print()
	cv2.imshow("ori",image)
	cv2.imshow("mask",mask)
	cv2.imshow("gray",gray)
	cv2.waitKey(0)
	cv2.destroyAllWindows

print(x)
print("Highest rice count:"+str(max(x)))
plt.hist(x)
plt.show()