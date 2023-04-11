import cv2 as cv

img = cv.imread('noise.png')
#blur = cv.GaussianBlur(img,(41,41),sigmaX= 3, sigmaY= 3)
#cv.imshow('blur', blur)
cv.imshow('img', img)

#applying bilateral filter
bilat = cv.bilateralFilter(img,15,50,75, borderType=cv.BORDER_CONSTANT)
cv.imshow('bilat', bilat)
cv.waitKey(0)

