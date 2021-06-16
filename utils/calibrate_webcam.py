import cv2

def calibrate():
	vid = cv2.VideoCapture(0)
	x,y,h,w = 45,5,440,465

	while(True):
		ret, frame = vid.read()
		img = frame[y:y+h,x:x+w]
		cv2.imshow("webcam",img)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.imwrite("test.jpg",img)
			cv2.destroyAllWindows()
			break

		
	vid.release()

calibrate()