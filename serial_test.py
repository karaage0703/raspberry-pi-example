import serial
import time

ser = serial.Serial("/dev/ttyS0", 115200)

while True:
    ser.write(bytes("hello", 'UTF-8'))
    time.sleep(0.01)

ser.close()
