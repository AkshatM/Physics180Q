import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = 2*np.array([2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,3]) # at 97 mm
xvalues = float(3.334/50000)*np.array([4000,3990,3880,3800,3600,3220,2660,2150,1450,971,545,11])-float(3.334*5/50000)
myrange2 = 2*np.array([2.25,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9]) 
xvalues2 = float(3.334/50000)*np.array([4200,4170,3960,3250,2230,1330,584,196,29,11])-float(3.334*5/50000)
myrange3 = 2*np.array([2.85,2.9,2.95,3,3.05,3.10,3.15,3.2,3.25,3.3,3.35,3.40,3.45])
xvalues3 = float(3.334/50000)*np.array([4200,4150,4000,3790,3200,2540,1800,1030,584,252,128,33,13])-float(3.334*5/50000)

def power_function1(x, w, d):
    return (xvalues[0]/2.00)*(1 - erf(pow(2,0.5)*(x+d)/w))

def power_function2(x, w, d):
    return (xvalues2[0]/2.00)*(1 - erf(pow(2,0.5)*(x+d)/w))

def power_function3(x, w, d):
    return (xvalues3[0]/2.00)*(1 - erf(pow(2,0.5)*(x+d)/w))

poptx, pcov = curve_fit(power_function1, myrange, xvalues, p0 = [0.55, -np.mean(myrange)])
poptx2, pcov2 = curve_fit(power_function2, myrange2, xvalues2, p0 = [0.59,-np.mean(myrange2)])
poptx3, pcov3 = curve_fit(power_function3, myrange3, xvalues3, p0 = [0.53, -np.mean(myrange3)])

print poptx, np.mean(myrange)
print poptx2, np.mean(myrange2)
print poptx3, np.mean(myrange3)

plt.figure()
plt.suptitle('Power as a Function of Knife Blade Displacement After Telescope')
plt.subplot(131)
plt.title(r'$P(x)$ at 150 mm')
plt.plot(myrange,xvalues,'rx')
plt.plot(np.arange(myrange[0],myrange[-1],0.01),power_function1(np.arange(myrange[0],myrange[-1],0.01),poptx[0], poptx[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(132)
plt.title(r'$P(x)$ at 270 mm')
plt.plot(myrange3,xvalues3,'rx')
plt.plot(np.arange(myrange3[0],myrange3[-1],0.01),power_function3(np.arange(myrange3[0],myrange3[-1],0.01),poptx3[0], poptx3[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(133)
plt.title(r'$P(x)$ at 495 mm')
plt.plot(myrange2,xvalues2,'rx')
plt.plot(np.arange(myrange2[0],myrange2[-1],0.01),power_function2(np.arange(myrange2[0],myrange2[-1],0.01),poptx2[0], poptx2[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.show()

