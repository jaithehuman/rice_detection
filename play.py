from imutils import contours
import imutils
import cv2
import numpy as np
from numpy.core.fromnumeric import reshape
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag
import sys
from imutils import perspective
from scipy.spatial import distance as dist


filename = sys.argv[1]
image = cv2.imread(filename)
img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

cv2.imshow("gray",gray)

edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)

rice = str(len(cnts))
print(rice)

cv2.drawContours(img,cnts,-1,(0,255,0),2)

# cv2.imshow('thresh',thresh)
cv2.imshow('edge',edged)
cv2.imshow('image',image)
cv2.imshow('ori',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
