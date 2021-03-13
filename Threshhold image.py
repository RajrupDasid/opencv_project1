import cv2 as cv

img = cv.imread('Photos/Butterfly.jpg')
cv.imshow('Manvswild',img)
#simple thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#threshholding
threshold,thresh=cv.threshold(gray,100,255, cv.THRESH_BINARY)
cv.imshow("Gray Thresholded", thresh)

#thresh binary inverse
threshold,thresh_inv=cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded inverse", thresh_inv)

#Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholdting', adaptive_thresh)



cv.waitKey(0)
