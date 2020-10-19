#!/usr/bin/env python

'''
Taken from : http://acodigo.blogspot.com/2017/08/histogramas-opencv-python.html
'''

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../resources/lena.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Lena',img)

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv.destroyAllWindows()

