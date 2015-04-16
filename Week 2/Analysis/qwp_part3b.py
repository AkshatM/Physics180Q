import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(t),4)

def f2(t):
    return pow(-np.sin(t),4)

myrange = np.arange(0,190,10)
values1 = float(3.334/10000)*np.array([1190,1430,1700,1810,1860,1810,1670,1370,1000,653,400,210,136,159,237,400,601,819,1180])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([0,0,0,0,0,0,0,0,0,3,0,1,2,2,2,0,1,1,0])

plt.figure(1)
plt.suptitle('Circular Beams - QWP Followed By QWP')
plt.subplot(121)
plt.title('Power Through First Arm')
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degrees)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.errorbar(myrange, values2, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.title('Experiment')
plt.ylim((0,0.63))
plt.subplot(122)
plt.title(r'Theory = $\cos^{4}(t)$')
plt.plot(myrange,f1(np.radians(myrange)))
plt.plot(myrange,f2(np.radians(myrange)))
plt.xlabel('Angle (Degrees)')
plt.show()
