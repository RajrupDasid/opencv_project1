import cv2 as cv
import numpy as np
img = cv.imread('Photos/BG.jpg')
cv.imshow('Bear', img)
blank =  np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)
mask = cv.circle(blank, (img.shape[1]//2 +30 ,img.shape[0]//2 -90), 200, 255, -1)
cv.imshow('Mask',mask)
masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('Masked Image', masked)
cv.waitKey(0)