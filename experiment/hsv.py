from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

img = cv2.imread("./dataset/variety.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

def count_color(cnts):
    count = 0
    for c in cnts:
        if cv2.contourArea(c) > 200 and cv2.contourArea(c) > 450:
            count = count + 10
        elif cv2.contourArea(c) > 50 and cv2.contourArea(c) < 200:
            count = count + 1
    return count


def contour_draw(mask):
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # print(cnts)
    if cnts == []:
        print()
    else:
        (cnts, _) = contours.sort_contours(cnts)   
    return cnts
#Red jasmine rice
lower_red = np.array([0,0,0])
upper_red = np.array([30,255,255])
mask = cv2.inRange(hsv,lower_red,upper_red)
cv2.imshow("mask",mask)
cv2.waitKey(0)
contours_red = contour_draw(mask)
count_red = count_color(contours_red)

#Yellow brown rice
lower_yellow = np.array([30,50,90])
upper_yellow = np.array([50,255,255])
mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
# cv2.imshow("mask",mask)
# cv2.waitKey(0)
contours_yellow = contour_draw(mask)
count_yellow = count_color(contours_yellow)

#White sticky rice
lower_white = np.array([50,0,120])
upper_white = np.array([100,255,255])
mask = cv2.inRange(hsv,lower_white,upper_white)
# cv2.imshow("mask",mask)
# cv2.waitKey(0)
contours_white = contour_draw(mask)
count_white = count_color(contours_white)

#count
count_array = [0,0,0]
count_array[0] = count_yellow
count_array[1] = count_red
count_array[2] = count_white
rice_type = ["brown rice","red jasmine rice","sticky rice"]

# print(count_array)
# print("yellow:",count_yellow)
# print("red:",count_red)

print("Type:")
for i in range(len(count_array)):
    # print(i)
    if count_array[i] > 0:
        print(rice_type[i],":",count_array[i])
        cv2.putText(img,str(rice_type[i]) + ":" + str(count_array[i]),(0,300+(i*50)),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0), 1)
cv2.imshow("ori",img)
# cv2.imshow("HSV",hsv)
# cv2.imshow("Gray",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()