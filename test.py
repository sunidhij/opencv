import cv2 as cv
#Rescaling 
#works for images, videos and live videos 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

#reading videos
#0,1,2... used for webcams
capture = cv.VideoCapture(0)
#a while loop is used to run the video frame by frame

#only for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height )

if not capture.isOpened():
    raise IOError("Cannot open webcam")

while True:
    isTrue, frame = capture.read()
    #frame_resized = rescaleFrame(frame)
    #for showing single frame
    cv.imshow('video', frame)
   # cv.imshow('video resized', frame_resized )
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()