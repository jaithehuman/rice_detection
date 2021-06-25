from imutils import contours
import imutils
import cv2
import numpy as np
from numpy.core.fromnumeric import reshape


image = cv2.imread('testtt.jpg')
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,180], dtype=np.uint8)
upper_white = np.array([180,50,255], dtype=np.uint8)

mask = cv2.inRange(hsv,lower_white,upper_white)
res = cv2.bitwise_and(image,image,mask=mask)

open = cv2.morphologyEx(
        res,
        cv2.MORPH_OPEN,
        np.ones((7,7),
        np.uint8),
        iterations=1)

cv2.imshow("ori",image)
cv2.imshow("mask",mask)
cv2.imshow("res",res)
cv2.imshow("open",open)
cv2.waitKey(0)
cv2.destroyAllWindows