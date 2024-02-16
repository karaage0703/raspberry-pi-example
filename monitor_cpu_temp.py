import os
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return float(temp) / 1000

temps = []

def update(frame):
    temp = get_cpu_temp()
    temps.append(temp)
    plt.cla()
    plt.plot(temps)
    plt.title("CPU Temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")

ani = FuncAnimation(plt.gcf(), update, interval=1000)

plt.tight_layout()
plt.show()

