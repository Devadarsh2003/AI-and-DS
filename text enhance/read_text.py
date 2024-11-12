import cv2 as cv

image = cv.imread("text enhance/sample.jpg")
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

ret, thresh = cv.threshold(image, 51, 255, cv.THRESH_BINARY)
adaptive = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 151, 3)

cv.imshow("thresholding",thresh)
cv.imshow("adaptive",adaptive)
cv.imshow("image",image)

cv.waitKey(0)
cv.destroyAllWindows()