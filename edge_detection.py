import cv2 as cv
import numpy as np 

camera = cv.VideoCapture(0)

while True:

    ret, frame = camera.read()
    
    if ret:
        laplacian = cv.Laplacian(frame,cv.CV_64F)
        laplacian = np.uint8(laplacian)
        cv.imshow('laplacian', laplacian)

        canny = cv.Canny(frame,100,100)
        cv.imshow('canny',canny)

        if cv.waitKey(5) == ord('x'):
            break

cv.destroyAllWindows()
camera.release()
