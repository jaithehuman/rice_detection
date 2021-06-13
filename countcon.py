from imutils import contours
import imutils
import cv2



image = cv2.imread('test.jpg')
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

print("count:", rice)
print()

cv2.drawContours(image,cnts,-1,(0,255,0),3)
cv2.imshow("exp",image)
cv2.imshow("edge",edged)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows