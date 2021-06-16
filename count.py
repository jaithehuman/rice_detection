import cv2

 # Read
img_rice = cv2.imread("./exp/test4/5.jpg")
cv2.imshow('rice', img_rice)
 # Grayscale 
img_gray = cv2.cvtColor(img_rice, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img_gray)
 # Binarization 
ret,thresh1 = cv2.threshold(img_gray, 123, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh1)

 # Corrosion and expansion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2)) #define rectangular structure element

img_erode = cv2.erode(thresh1, kernel, iterations=3)
cv2.imshow('erode', img_erode)

img_dilated = cv2.dilate(img_erode, kernel)
 # Edge detection
contours, hierarchy = cv2.findContours(img_dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

count = 0
ave_area = 0
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area > 20:
        
        count = count + 1
        ave_area = ave_area + area
        rect = cv2.boundingRect(contours[i]) #Extract rectangle coordinates

        print("number:{} x:{} y:{} area:{}".format(count,rect[0],rect[1], area))#Print coordinates

        cv2.rectangle(img_rice,rect,(0,255,0),1)#Draw a rectangle
        if area > 150:
            count = count + 1
            # cv2.putText(img_rice,str({count,count-1}), (rect[0], rect[1]), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1) #In the upper left corner of the rice grain Write number
        else:
            pass
            # cv2.putText(img_rice,str(count), (rect[0], rect[1]), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1) #Write the number in the upper left corner of the rice grain

    
ave_area = ave_area / count
 # Output
print('The total number is: {}, the average area is: {}'.format(count,ave_area))
cv2.imshow("Contours", img_rice)

cv2.waitKey(0)
cv2.destroyAllWindows()