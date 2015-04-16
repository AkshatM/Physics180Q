import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(2*t),2)

def f2(t):
    return pow(np.cos(2*t),2)

myrange = np.arange(0,190,10)
values1 = float(3.334/10000)*np.array([1310,975,633,440,582,814,1200,1410,1430,1210,876,594,405,562,817,1200,1440,1440,1200])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([0,2,2,3,2,2,0,0,0,0,3,0,1,2,1,0,0,0,0])

plt.figure(1)
plt.ylabel('Power (mW)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.errorbar(myrange, values2, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.plot(myrange, float(3.334/20000)*1910*np.ones(values1.shape), 'r')
plt.title('Power Through First Arm (Blue); Power Through Second Arm (Green)')
plt.ylim((0,0.63))
plt.suptitle('Elliptical Beams - QWP Followed By HWP')
plt.show()
