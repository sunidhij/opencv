import cv2 as cv
import numpy as np

cat = cv.imread('cat.jpg')
panda = cv.imread('panda.jpg')


#addition
#res = cv.add(cat, panda)
#res1 = cv.addWeighted(cat,0.7, panda,0.3,0)
#cv.imshow('cat', cat)
#cv.imshow('panda', panda)
#cv.imshow('res', res)
#cv.imshow('res1', res1)

#subtraction
#res = cv.subtract(panda, cat)
#cv.imshow('res', res)

#multiplication
res = np.multiply(cat, panda)
res2 = cv.multiply(cat, panda)

cv.imshow('res', res)
cv.imshow('res2', res2)

#divide
#res = np.divide(panda, cat)
#res2 = cv.divide(cat, panda)

#cv.imshow('res', res)
#cv.imshow('res2', res2)



cv.waitKey(0)