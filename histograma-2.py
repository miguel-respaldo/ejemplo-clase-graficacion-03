#!/usr/bin/env python

'''
Taken from : http://acodigo.blogspot.com/2017/08/histogramas-opencv-python.html
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
cv.imshow('Lena',img)

color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show()

cv.destroyAllWindows()
