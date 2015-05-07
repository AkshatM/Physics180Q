import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = 2*np.array([1.25,1.5,1.75,1.8,1.85,1.9,1.95,2,2.25,2.5]) # at 97 mm
xvalues = float(3.334/10000)*np.array([151,149,108,89,67.7,46.9,29.4,17.5,1.23,0.700])-float(3.334*0.6/10000)
myrange2 = 2*np.array([1,1.25,1.5,1.6,1.75,1.8,1.85,1.9,1.95,2,2.25]) 
xvalues2 = float(3.334/10000)*np.array([133,133,127,120,77,60,44,29.3,16.8,8.2,0.730])-float(3.334*0.6/10000)
myrange3 = 2*np.array([1.5,1.75,1.8,1.85,1.9,1.95,2,2.1,2.25,2.5])
xvalues3 = float(3.334/10000)*np.array([127,104,95,75,57,40,22.3,7.7,0.78,0.6])-float(3.334*0.6/10000)

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
plt.title(r'$P(x)$ at 97 mm')
plt.plot(myrange,xvalues,'rx')
plt.plot(np.arange(myrange[0],myrange[-1],0.01),power_function1(np.arange(myrange[0],myrange[-1],0.01),poptx[0], poptx[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(132)
plt.title(r'$P(x)$ at 473 mm')
plt.plot(myrange2,xvalues2,'rx')
plt.plot(np.arange(myrange2[0],myrange2[-1],0.01),power_function2(np.arange(myrange2[0],myrange2[-1],0.01),poptx2[0], poptx2[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.subplot(133)
plt.title(r'$P(x)$ at 890 mm')
plt.plot(myrange3,xvalues3,'rx')
plt.plot(np.arange(myrange3[0],myrange3[-1],0.01),power_function3(np.arange(myrange3[0],myrange3[-1],0.01),poptx3[0], poptx3[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.show()
