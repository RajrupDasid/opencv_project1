#Gradients
import cv2 as cv
import numpy as np

img = cv.imread('Photos/Butterfly.jpg')
cv.imshow('Butterfly',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#location
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel x",sobelx)
cv.imshow("Sobel y",sobely)
cv.imshow("Combined_sobel", combined_sobel)

canny = cv.Canny(gray,160,180)
cv.imshow("Canny", canny)
cv.waitKey(0)