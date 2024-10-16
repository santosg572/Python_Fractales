import numpy as np
import matplotlib.pyplot as plt

def EncuentraMaximo():
  np1 = 101
  img = np.zeros((np1, np1))

  ma = 0
  for i in range(np1):
    x = 4*i/(np1-1) -2
    for k in range(np1):
      y = 4*k/(np1-1) - 2
      c = complex(x, y)
      z = complex(0,0)
      for m in range(10):
        z = z**2 + c
      val = np.abs(z)
      if val < 1000:
        img[i,k] = 1
        if val > ma:
          ma = val
  print(ma)
  return ma


def GeneraMadel(ma = 0):
  np1 = 101
  img = np.zeros((np1, np1))

  ma = 0
  for i in range(np1):
    x = 4*i/(np1-1) -2
    for k in range(np1):
      y = 4*k/(np1-1) - 2
      c = complex(x, y)
      z = complex(0,0)
      for m in range(10):
        z = z**2 + c
      val = np.abs(z)
      if val < 1000:
        img[i,k] = 2*val/ma
        if val > ma:
          ma = val
  print(ma)
  return img

ma = EncuentraMaximo()
img = GeneraMadel(ma)

plt.imshow(img)
plt.show()

 
