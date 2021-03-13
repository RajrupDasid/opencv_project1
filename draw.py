import cv2 as cv
import numpy as np
blank = np.zeros((640,480,3), dtype='uint8')
#cv.imshow('Blank',blank)
blank[200:300, 400:500]=0,0,255
#draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness =-1 )
cv.imshow('Rectangle',blank)
cv.imshow('Red',blank)
#draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)

# add text on image
cv.putText(blank,"Hello World",(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)
