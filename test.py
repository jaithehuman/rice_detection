import cv2
import numpy
crop = cv2.imread("capture.jpg")
# coin width  65 pixel
# coin width 20 mm
# pixel per 20 mm = 65/20 = 3.25 pixel per 20 mm
# 
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret,thresh1 = cv2.threshold(blur,90,255,cv2.THRESH_BINARY)
edged = cv2.Canny(thresh1, 100, 255)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rice_count = str(len(contours))

print("No. RICE = " + rice_count)
cv2.drawContours(crop, contours, -1, (0, 255, 0), 3)    
cv2.putText(crop,"rice:" + rice_count,(0,440),1,2,color=(0,255,0),thickness=2)
cv2.imshow("res",thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()