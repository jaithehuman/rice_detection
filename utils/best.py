from imutils import contours
import imutils
import cv2
import numpy as np
from numpy.core.fromnumeric import reshape
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag

image = cv2.imread('test.jpg')
# image = cv2.imread('./exp/test7/8.jpg')
blur = cv2.GaussianBlur(image,(3,3),0)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#extract white
lower_white = np.array([0,0,180], dtype=np.uint8)
upper_white = np.array([179,255,255], dtype=np.uint8)

mask = cv2.inRange(hsv,lower_white,upper_white)
res = cv2.bitwise_and(image,image,mask=mask)
#gray
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 50, 100)
dilate = cv2.dilate(canny, None, iterations=1)
edged = cv2.erode(dilate, None, iterations=1)

#thres
_,thres = cv2.threshold(dilate,0,255,cv2.THRESH_BINARY)





contours
cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)


# ####old
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (7, 7), 0)

# canny = cv2.Canny(gray, 50, 100)
# dilate = cv2.dilate(canny, None, iterations=1)
# edged = cv2.erode(dilate, None, iterations=1)

# cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)

# (cnts, _) = contours.sort_contours(cnts)
rice = int(str(len(cnts)))

print(rice)

count = 0
# for c in cnts:
# 	if cv2.contourArea(c) < 150 and cv2.contourArea(c) > 30:
# 		count += 1
	# orig = image.copy()
	# print(cv2.contourArea(c))
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()
	# 	break
	# cv2.drawContours(orig,c,-1,(0,255,0),2)
	# cv2.imshow("image",orig)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

cv2.drawContours(image,cnts,-1,(0,255,0),2)

print(count)
cv2.imshow("ori",image)
cv2.imshow("gray",gray)
# cv2.imshow("canny",canny)
# cv2.imshow("dilate",dilate)
# cv2.imshow("edge",edged)
# cv2.imshow("blur",blur)
# cv2.imshow("mask",mask)
# cv2.imshow("hsv",hsv)
# cv2.imshow("res",res)
# cv2.imshow("gray",gray)
# cv2.imshow("open",opening)
cv2.imshow("thres",thres)
cv2.waitKey(0)
cv2.destroyAllWindows()