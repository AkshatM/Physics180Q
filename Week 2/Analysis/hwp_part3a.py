import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(2*t),2)

def f2(t):
    return pow(np.cos(2*t),2)

myrange = np.arange(0,190,10)
values1 = float(3.334/10000)*np.array([978,1020,1120,1110,1020,966,829,805,810,898,997,1030,1040,1010,970,868,842,905,995])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([1,0,0,1,0,3,1,1,2,2,0,0,0,0,2,2,3,3,0])

plt.figure(1)
plt.title('Power Through First Arm')
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degrees)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.errorbar(myrange, values2, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.plot(myrange, float(3.334/20000)*1910*np.ones(values1.shape), 'r')
plt.title('Power Through First Arm (Blue); Power Through Second Arm (Green)')
plt.ylim((0,0.63))
plt.suptitle('Circular Beams - QWP Followed By HWP')
plt.show()
