# -*- coding: utf-8 -*-
import shutter as sh
from time import sleep
import sys

if __name__ == '__main__':
    sh.setting()
    sh.camera.start_preview()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('interrupted!')
        sys.exit()