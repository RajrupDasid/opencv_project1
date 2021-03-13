import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Photos/Bear.jpeg')
cv.imshow('Bear', img)
blank = np.zeros(img.shape[:2], dtype='uint8')
circle= cv.circle(blank,(img.shape[1]//2 +30 ,img.shape[0]//2 -110 ), 190, 255, -1)
mask= cv.bitwise_and( img, img, mask=circle)
cv.imshow('Mask',mask)

#color histogram
plt.figure()
plt.title('Color scale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])


plt.show()

cv.waitKey(0)