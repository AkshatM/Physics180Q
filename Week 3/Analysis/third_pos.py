import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = np.array([1,1.25,1.5,1.75,1.8,1.85,1.9,1.95,2,2.25,2.5])
xvalues = float(3.334/10000)*np.array([0.4,7.5,280,997,1190,1400,1650,1810,2010,2680,2820])-float(3.334*15/10000)

def power_function(x, w, d):
    return (xvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(x+d)/w))

myrange2 = np.array([1,1.05,1.1,1.15,1.2,1.21,1.22,1.23,1.24,1.25,1.5,2.25])
yvalues = float(3.334/10000)*np.array([247,518,882,1270,1660,1830,1870,1920,1980,2082,2800,2820])-float(3.334*0.4/10000)

def power_function2(y, w, d):
    return (yvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(y+d)/w))

poptx, pcov = curve_fit(power_function, myrange, xvalues)
popty, pcov = curve_fit(power_function2, myrange2, yvalues)

print poptx, np.mean(myrange)
print popty, np.mean(myrange2)

plt.figure()
plt.suptitle('Power as a Function of Knife Blade Displacement - Third Position')
plt.subplot(121)
plt.title(r'$P(x)$')
plt.plot(myrange,xvalues,'rx')
plt.plot(myrange,power_function(myrange,poptx[0],poptx[1]))
plt.ylim((0,1))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (cm)')
plt.subplot(122)
plt.title(r'$P(y)$')
plt.plot(myrange2,yvalues,'rx')
plt.plot(myrange2,power_function2(myrange2,popty[0],popty[1]))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (cm)')
plt.ylim((0,1))
plt.show()

