import cv2 as cv
import numpy as np

#Gaussian Blur
#OpenCv can perfrom this using cv.GaussianBlur()

cat = cv.imread('cat.jpg')
cv.imshow('cat',cat)

#Applying Filter
blur = cv.GaussianBlur(cat,(41,41),sigmaX= 3, sigmaY= 20)
cv.imshow('blur', blur)

cv.waitKey(0)
 
#to write image
#cv.imwrite('blur.jpg', blur)