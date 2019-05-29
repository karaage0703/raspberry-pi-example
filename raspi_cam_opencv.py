# coding: utf-8
# raspi cam demo
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)

count_max = 0

if __name__ == '__main__':
    count = 0

    stream = PiRGBArray(camera)
    while True:
        camera.capture(stream, 'bgr', use_video_port=True)
        img = stream.array

        key = cv2.waitKey(1)
        if key == 27: # when ESC key is pressed break
            break

        count += 1
        if count > count_max:
            cv2.imshow('View', img)
            count = 0

        stream.seek(0)
        stream.truncate()

    camera.close()
    cv2.destroyAllWindows()
