import numpy as np
import cv2
import time
def run():
    capture = cv2.VideoCapture("rtsp://admin:abc12345@192.168.137.12:554/onvif1", cv2.CAP_FFMPEG)
    #capture .set(cv.CV_CAP_PROP_FOURCC, cv.CV_FOURCC('H', '2', '6', '4'))
    while True:
        result, frame = capture.read()
        frame=cv2.resize(frame,(512,250))
        cv2.imshow('video', frame)

        if cv2.waitKey(16) == ord("q"):
            break