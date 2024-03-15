import numpy as np
import matplotlib.pyplot as plt

A = 1
F = 2
B = 0
T = np.arange(0, 3, 0.01)
class DrawSin:
  def __init__(self, F, A=1, END_TIME=5, B=0, INTERVAL=0.01):
    self.T = np.arange(0, END_TIME, INTERVAL)
    self.y = A * np.sin(2 * np.pi * self.calc(F) * self.T) + B

  def draw(self):
    plt.figure()
    plt.plot(self.T, self.y)
    plt.title('Sine Wave')
    plt.show()

class DrawCos(DrawSin):
  def calc(self, F):
    return np.sin(2 * np.pi * F * self.T)

d = DrawCos(5);
d.draw()
