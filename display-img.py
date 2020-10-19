#!/usr/bin/env python

'''
Taken from : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
'''

import cv2 as cv
import numpy as np

img = cv.imread('../resources/lena.jpg',0)

#print(img)

cv.imshow('Lena',img)
print("Oprime ESC para salir")

while True:
  k = cv.waitKey(0)

  if k == 27:         # wait for ESC key to exit
    break
  elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('lena-gray.png',img)
    print("Imagen guardada")

cv.destroyAllWindows()
