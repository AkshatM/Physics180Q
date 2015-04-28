import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = 2*np.array([2,2.15,2.20,2.21,2.22,2.23,2.24,2.25,2.3,2.35,2.5])
xvalues = float(3.334/10000)*np.array([38,157,660,880,1080,1240,1440,1530,2050,2130,2200])-float(3.334*10/10000)
myrange2 = 2*np.array([0.45,0.5,0.51,0.52,0.55,0.58,0.6,0.62,0.65,0.7])
xvalues2 = float(3.334/10000)*np.array([105,440,580,725,1080,1330,1530,1840,2090,2200])-float(3.334*10/10000)
myrange3 = 2*np.array([2,2.25,2.35,2.4,2.5,2.53,2.55,2.6,2.7,2.75,3,3.25])
xvalues3 = float(3.334/10000)*np.array([30,123,250,356,800,998,1140,1480,1870,1970,2130,2180])-float(3.334*10/10000)

def power_function(x, w, d):
    return (xvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(x+d)/w))

poptx, pcov = curve_fit(power_function, myrange, xvalues, p0 = [0.196, -np.mean(myrange)])
poptx2, pcov2 = curve_fit(power_function, myrange2, xvalues2, p0 = [0.3, -np.mean(myrange2)])
poptx3, pcov3 = curve_fit(power_function, myrange3, xvalues3, p0 = [0.6, -np.mean(myrange3)])

print poptx, np.mean(myrange)
print poptx2, np.mean(myrange2)
print poptx3, np.mean(myrange3)

plt.figure()
plt.suptitle('Power as a Function of Knife Blade Displacement After Telescope')
plt.subplot(131)
plt.title(r'$P(x)$ at 392 mm')
plt.plot(myrange,xvalues,'rx')
plt.plot(np.arange(myrange[0],myrange[-1],0.01),power_function(np.arange(myrange[0],myrange[-1],0.01),poptx[0], poptx[1]))
plt.ylim((0,1))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(132)
plt.title(r'$P(x)$ at 113 mm')
plt.plot(myrange2,xvalues2,'rx')
plt.plot(np.arange(myrange2[0],myrange2[-1],0.01),power_function(np.arange(myrange2[0],myrange2[-1],0.01),poptx2[0], poptx2[1]))
plt.ylim((0,1))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(133)
plt.title(r'$P(x)$ at 780 mm')
plt.plot(myrange3,xvalues3,'rx')
plt.plot(np.arange(myrange3[0],myrange3[-1],0.01),power_function(np.arange(myrange3[0],myrange3[-1],0.01),poptx3[0], poptx3[1]))
plt.ylim((0,1))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.show()
