import cv2 as cv

video = cv.VideoCapture("people.mp4")
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

while True:

    ret, frame = video.read()

    if ret:
         mask = subtractor.apply(frame)
         cv.imshow('mask',mask)

         if cv.waitKey(5) == ord('x'):
            break
    
    else:
        video = cv.videoCapture('people.mp4')

cv.destroyAllWindows()
video.release()