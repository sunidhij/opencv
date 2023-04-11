import cv2 as cv
import numpy as np


cat = cv.imread('cat.jpg')
cat2 =cv.imread('cat - Copy.jpg')

cv.imshow( 'cat', cat)
cv.imshow( 'cat2', cat2)

cv.waitKey(0)

