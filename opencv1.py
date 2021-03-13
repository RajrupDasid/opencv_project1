import cv2 as cv

#reading videos
capture = cv.VideoCapture('Videos/dog.mp4')
def rescaleFrame(frame, scale=0.2):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
while True:
    isTrue, frame= capture.read()
    #cv.imshow('Video',frame)
    frame_resized=rescaleFrame(frame)
    #cv.imshow('video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)