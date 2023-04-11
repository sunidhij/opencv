import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray) 

canny = cv.Canny(gray, 95, 105)
cv.imshow('canny',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))       

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# ret, thresh = cv.threshold(gray,135, 255, cv.THRESH_BINARY)


# cv.imshow('cat',thresh)
cv.waitKey(0)

