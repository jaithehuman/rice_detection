from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def filter(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)

	edged = cv2.Canny(gray, 50, 100)
	edged = cv2.dilate(edged, None, iterations=1)
	edged = cv2.erode(edged, None, iterations=1)
	
	return edged

def find_contour(img):
	cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
	(cnts, _) = contours.sort_contours(cnts)
	return cnts

def compute(cnts,image):
	pixelsPerMetric = None
	count = 0
	rice = 0
	rice = str(len(cnts))
	rice= int(rice) - 1
	for c in cnts:
		group = False
		if cv2.contourArea(c) < 50:
			continue
		elif cv2.contourArea(c) > 200:
			if count != 0:
				group = True
		orig = image.copy()
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
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

		if dimA > dimB:
		# print("swap")
			temp = dimA
			dimA = dimB
			dimB = temp
		
		print()	
		if group == True:
			print("group of rice")
			print()
			cv2.putText(orig,"Group of rice",(int(tltrX - 15), int(tltrY - 10)),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 255), 2)
		elif group == False:
			print("Rice_" + str(count))
			print("width :{:.2f}cm".format(dimA * 2.54))
			print("height:{:.2f}cm".format(dimB * 2.54))
			cv2.putText(orig, "{:.2f}cm".format(dimA * 2.54),
				(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
				0.65, (255, 255, 255), 2)
			cv2.putText(orig, "{:.2f}cm".format(dimB * 2.54),
				(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
				0.65, (255, 255, 255), 2)
		cv2.putText(orig,"Rice:"+ str(rice),(0,440),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0), 2)
		# show output 
		# print(count)
	count += 1
	return orig

def main():
	path_image = cv2.imread(".\dataset\size3.jpg")
	img = filter(path_image)
	cnt = find_contour(img)
	res = compute(cnt,path_image)
	cv2.imshow("Measuring_Size_Image", res)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()
