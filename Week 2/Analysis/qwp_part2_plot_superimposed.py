import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return pow(np.sin(2*t),2)

def f2(t):
    return pow(np.cos(2*t),2)

myrange = np.arange(0,370,10)
values1 = float(3.334/10000)*np.array([997,1260,1600,1780,1690,1410,1170,940,878,1050,1330,1610,1780,1666,1400,1110,
          840,807,1000,1400,1790,1910,1820,1610,1250,1020,996,1190,1430,1800,1900,1810,1600,1200,999,946,1140])
values2 = float(3.334/10000)*1910*np.ones(values1.shape) - values1
yerr = float(3.334/10000)*np.array([1,0,0,0,0,0,1,2,2,0,0,0,0,0,0,0,3,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0])

plt.figure(1)
plt.suptitle('Superimposed Power Versus Angle - Quarter Wave Plate Experiment')
plt.title('Power Through First Arm (Blue); Power Through Second Arm (Green)')
plt.errorbar(myrange, values1, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.errorbar(myrange, values2, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degrees)')
plt.xlim((0,360))
plt.show()

