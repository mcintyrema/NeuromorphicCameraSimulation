# cv2 used to perform operations on videos
import numpy as np
numpy = np
import cv2

# creating a video capture object
vid = cv2.VideoCapture(0)  # first webcam
if not vid.isOpened():
    raise IOError("Cannot open webcam")

ret, frame1 = vid.read()

while ret == 0:
    # Capture frame by frame
    #previous frame
    ret, frame1 = vid.read()
    # converting frames to grayscale
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

pixelThrespos = 40
pixelThresneg = -40

t = 200

for k in range(t):
    ret, frame2 = vid.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    img = frame1-frame2

    #difference between color values of pixels in frame
    diffThresh = gray.astype(np.int8) - gray2.astype(np.int8)

    #changing color values
    yblack, xblack = np.where(diffThresh > pixelThrespos) #locating pixels
    img[yblack, xblack] = np.asarray([255])

    ywhite, xwhite = np.where(diffThresh < pixelThresneg)
    img[ywhite, xwhite] = np.asarray([0])

    ygray, xgray = np.where((diffThresh > pixelThresneg) & (diffThresh < pixelThrespos))
    img[ygray, xgray] = np.asarray([128])

    cv2.imshow('frame', img)

    cv2.waitKey(1)

    frame1 = frame2



