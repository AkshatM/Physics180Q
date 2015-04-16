import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(2*t),2)

def f2(t):
    return pow(np.cos(2*t),2)

myrange = np.arange(0,370,10)
values1 = float(3.334/10000)*np.array([619,204,110,400,880,1420,1760,1590,1120,540,193,128,400,960,1460,1770,
          1580,1060,478,158,174,415,1060,1560,1780,1470,977,401,149,176,448,1080,1560,1760,1450,1000,404])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([2,2,0,5,0,1,0,0,5,2,3,0,3,0,0,0,0,2,2,2,5,0,0,0,0,2,1,3,1,3,0,1,1,1,0,1,3])

plt.figure(1)
plt.suptitle('Power Versus Angle - Half Wave Plate Experiment')
plt.subplot(221)
plt.title('Power Through First Arm')
plt.ylabel('Power (mW)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.xlim((0,360))
plt.subplot(222)
plt.plot(myrange,f1(np.radians(myrange)))
plt.title(r'$\sin^{2}(2\theta)$')
plt.xlim((0,360))
plt.subplot(223)
plt.errorbar(myrange, values2, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.title('Power Through Second Arm')
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degrees)')
plt.xlim((0,360))
plt.ylim((0,0.63))
plt.subplot(224)
plt.plot(myrange,f2(np.radians(myrange)))
plt.title(r'$\cos^{2}(2\theta)$')
plt.xlabel('Angle (Degrees)')
plt.xlim((0,360))
plt.show()
