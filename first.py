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

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

filename = sys.argv[1]
image = cv2.imread(filename)
img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

(cnts, _) = contours.sort_contours(cnts)

pixelsPerMetric = None

size = 0
for c in cnts:
	if cv2.contourArea(c) < 20 :
			continue
	size += 1
W = [0]*size
H = [0]*size


print(size)


pos = 0
first = True
for c in cnts:
	if first is False:
		if cv2.contourArea(c) < 20 :
			continue
	
	# print(cv2.contourArea(c))
	orig = image.copy()
	box = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	box = np.array(box, dtype="int")

	box = perspective.order_points(box)
	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 64), 2)

	for (x, y) in box:
		cv2.circle(orig, (int(x), int(y)), 5, (0, 255, 64), -1)
		

	(tl, tr, br, bl) = box
	(tltrX, tltrY) = midpoint(tl, tr)
	(blbrX, blbrY) = midpoint(bl, br)

	(tlblX, tlblY) = midpoint(tl, bl)
	(trbrX, trbrY) = midpoint(tr, br)

	cv2.circle(orig, (int(tltrX), int(tltrY)), 0, (0, 255, 64), 0)
	cv2.circle(orig, (int(blbrX), int(blbrY)), 0, (0, 255, 64), 0)
	cv2.circle(orig, (int(tlblX), int(tlblY)), 0, (0, 255, 64), 0)
	cv2.circle(orig, (int(trbrX), int(trbrY)), 0, (0, 255, 64), 0)

	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 255, 255), 1)
	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 255, 255), 1)

	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

	if pixelsPerMetric is None:
		pixelsPerMetric = dB / 0.787402

	dimA = dA / pixelsPerMetric
	dimB = dB / pixelsPerMetric
	
	
	# dimA is width
	# dimB is height
	if dimA < dimB:
		# print("swap")
		temp = dimA
		dimA = dimB
		dimB = temp
	
	width = round(dimA * 25.4,2)
	height = round(dimB * 25.4,2)
	if first is False:
		W[pos] = width
		H[pos] = height
		pos += 1
		print("rice_"+str(pos))

	first = False
	print("width:"+str(width)+"mm")
	print("height:"+str(height)+"mm")
	cv2.putText(orig, "{:.2f}mm".format(dimA * 25.4),
		(int(tltrX - 10), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	cv2.putText(orig, "{:.2f}mm".format(dimB * 25.4),
		(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)

	
	
	cv2.imshow("Measuring_Size_Image", orig)
	cv2.waitKey(0)

if 0 in W or H:
	while 0 in W :
		W.remove(0)
	while 0 in H :
		H.remove(0)

# print(len(W))
print(W)
print(H)

a=[5,5.5,6,6.5,7,7.5,8]
b=[1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6]

plt.title("Rice Width")
plt.xlabel('Width(mm)')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)
plt.hist(W,a)
plt.show()
plt.title("Rice Heigth")
plt.xlabel('Heigth(mm)')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)
plt.hist(H,b)
plt.show()