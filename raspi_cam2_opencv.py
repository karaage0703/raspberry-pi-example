# coding: utf-8
# raspi cam2 demo
import cv2

from picamera2 import Picamera2
from libcamera import controls

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()
camera.set_controls({'AfMode': controls.AfModeEnum.Continuous})

count_max = 0

if __name__ == '__main__':
    count = 0

    while True:
        img = camera.capture_array()

        key = cv2.waitKey(1)
        if key == 27: # when ESC key is pressed break
            break

        count += 1
        if count > count_max:
            cv2.imshow('View', img)
            count = 0

    camera.close()
    cv2.destroyAllWindows()
