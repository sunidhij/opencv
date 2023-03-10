import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('blank', blank)

#img = cv.imread('cat.jpg')
#cv.imshow('cat', img)

#two ways to draw - on image, or on dummy image

#paint the image a certain color
#blank[:]= 120,40,160 #whole screen
#blank[200:300, 350:400]= 120,40,160 #range

#draw a rectangle
#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=5)
#for filled rectangle, thickness = cv.FILLED OR -1

#Drawing a circle
#cv.circle(blank, (300,300),40, (0,255,0), thickness=5)

#drawing a line 
#cv.line(blank, (50,50), (200,200), (255,255,255), thickness=3)

#text on image
cv.putText(blank,'Hi', (250,250),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), thickness=2 )
 
cv.imshow('Green', blank)  
cv.waitKey(0) 