import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(2*t),2)

def f2(t):
    return pow(np.cos(2*t),2)

myrange = np.arange(0,190,10)
values1 = float(3.334/10000)*np.array([1220,746,340,21,184,542,1040,1410,1520,1200,757,325,22,184,525,1040,1410,1540,1200])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([0,3,3,1,1,2,0,0,1,0,3,3,3,2,3,0,0,0,0])

plt.figure(1)
plt.title('Power Through Polariser Arm')
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degree)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.show()
