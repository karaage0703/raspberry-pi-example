#!/usr/bin/python
# -*- coding: utf-8 -*-
import pigpio
import time

pin_numb = 18

pi = pigpio.pi()
pi.set_mode(pin_numb, pigpio.OUTPUT)

pi.set_servo_pulsewidth(pin_numb, 1000)
