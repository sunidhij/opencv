import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
cv.imshow('img', img)

#Average blurring

cv.waitKey(0)