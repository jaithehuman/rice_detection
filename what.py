import cv2


total = [5,3,5,6,7,8,4]
best = max(total)
pos = total.index(best)


image = cv2.imread(path +str(pos)+'.jpg')
