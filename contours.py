import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
img2 = cv.resize(img, (700,500))
gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(gray, 10, 105)

ret, thresh = cv.threshold(gray,135, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))       
cv.imshow('cat',thresh)
cv.waitKey(0)
