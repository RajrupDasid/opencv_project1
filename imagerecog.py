import cv2 as cv

img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat', img)
def rescaleFrame(frame, scale=0.2):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
resized_image= rescaleFrame(img)
cv.imshow('image',resized_image)
cv.waitKey(0)