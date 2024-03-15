import numpy as np
import matplotlib.pyplot as plt

class DrawSin:
  def __init__(self, F, A=1, END_TIME=5, B=0, INTERVAL=0.01):
    self.T = np.arange(0, END_TIME, INTERVAL)
    self.y = A * np.sin(2 * np.pi * self.calc(F) * self.T) + B
    self.name = 'Sine Wave'

  def calc(self, F):
    return np.sin(2 * np.pi * F * self.T)

  def draw(self):
    plt.figure()
    plt.plot(self.T, self.y)
    plt.title(self.name)
    plt.show()

class DrawCos(DrawSin):
  def __init__(self, F, A=1, END_TIME=5, B=0, INTERVAL=0.01):
    super().__init__(F, A, END_TIME, B, INTERVAL)
    self.name = 'Cosine Wave'

  def calc(self, F):
    return np.sin(2 * np.pi * F * self.T)

d = DrawSin(5);
d.draw()
