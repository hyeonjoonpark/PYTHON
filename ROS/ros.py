import numpy as np
import matplotlib
import matplotlib.pyplot as plt

A = 1
F = 2
B = 0
T = np.arange(0, 3, 0.01)

def drawSin(F, A=1, END_TIME=5, B=0, INTERVAL=0.01):
    T = np.arange(0, END_TIME, INTERVAL)
    y = A * np.sin(2 * np.pi * F * T) + B

    plt.figure()
    plt.plot(T, y)
    plt.show()

drawSin(3)
