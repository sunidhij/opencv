import cv2 as cv
import numpy as np

cat = cv.imread('cat.jpg')
dog = cv.imread('dog.jpg')

cv.imshow('cat', cat)
cv.imshow('dog', dog)

cv.waitKey(0)