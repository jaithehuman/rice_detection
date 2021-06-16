import cv2
import numpy
import sys

filename = sys.argv[1]
I = cv2.imread(filename, 0)
h,w = I.shape[:2]
diff = (3,3,3)
mask = numpy.zeros((h+2,w+2),numpy.uint8)
cv2.floodFill(I,mask,(0,0), (255,255,255),diff,diff)
T,I = cv2.threshold(I,180,255,cv2.THRESH_BINARY)
# I = cv2.medianBlur(I, 1)

totalrice = 0
oldlinecount = 0
for y in range(0, h):
    oldc = 0
    linecount = 0
    start = 0   
    for x in range(0, w):
        c = I[y,x] < 128;
        if c == 1 and oldc == 0:
            start = x
        if c == 0 and oldc == 1 and (x - start) > 10:
            linecount += 1
        oldc = c
    if oldlinecount != linecount:
        if linecount < oldlinecount:
            totalrice += oldlinecount - linecount
        oldlinecount = linecount
print(totalrice)
cv2.imshow('edged',I)
cv2.waitKey(0)
cv2.destroyAllWindows()