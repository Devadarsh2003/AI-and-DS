import pathlib
import cv2 as cv

cascade_path = pathlib.Path(cv.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

camera = cv.VideoCapture(0)

clf = cv.CascadeClassifier(cascade_path)

while True:
    _, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor = 1.1, 
        minNeighbors = 5,
        minSize = (30, 30), 
        flags = cv.CASCADE_SCALE_IMAGE
    )
    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2 )

    cv.imshow("faces", frame)
    if cv.waitKey(5) == ord('x'):
        break 

camera.release()
cv.destroyAllWindows()
