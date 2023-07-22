import os
import cv2
import detect as dt


def checkphoto():

    path = f'{os.getcwd()}//Chel'
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite(f'{path}//1.png', frame)
    cam.release()
    name = dt.detect(name = '1.png')
    return name

