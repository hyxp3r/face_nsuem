import cv2
import os
import prepare as pr

def makephoto(personalNumber):

    #book = str(input('Введите номер вашей зачетки: '))

    path = f'{os.getcwd()}//Images//{personalNumber}'
    os.mkdir(path)

    cam = cv2.VideoCapture(0)

    for pict in range(10):

        ret, frame = cam.read()
        cv2.imwrite(f'{path}//{pict}.png', frame)

    cam.release()

    len = pr.prepare()
    print(len)
    return len