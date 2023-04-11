import cv2 as cv

#reading the image
img = cv.imread('cat.jpg')

#creating a new window named Cat which opens the image
cv.imshow('Cat', img)

cv.waitKey(0) 

#----------------------------------------------

#Rescaling 
#works for images, videos and live videos 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_image = rescaleFrame(img, scale = 0.2)
cv.imshow('Img', resized_image )
#reading videos
#0,1,2... used for webcams
capture = cv.VideoCapture('video.mp4 ')
#a while loop is used to run the video frame by frame

#only for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height )

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    #for showing single frame
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized )


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()