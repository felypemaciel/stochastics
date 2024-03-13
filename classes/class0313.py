from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import math

A1 = random.normal(loc=0, scale=1)
A2 = random.normal(loc=0, scale=1)
A3 = random.normal(loc=0, scale=1)
A4 = random.normal(loc=0, scale=1)
A5 = random.normal(loc=0, scale=1)

t = np.linspace(0, 25, 100)

f = 0.1

f1 = A1*np.sin(2*np.pi*f*t)
f2 = A2*np.sin(2*np.pi*f*t)
f3 = A3*np.sin(2*np.pi*f*t)
f4 = A4*np.sin(2*np.pi*f*t)
f5 = A5*np.sin(2*np.pi*f*t)

plt.plot(t,f1, t,f2, t,f3, t,f4, t,f5)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()