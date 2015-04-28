import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = 2*np.array([1,1.25,1.45,1.5,1.6,1.75,2,2.25])
xvalues = float(3.334/10000)*np.array([22,398,1090,1740,1780,2330,2730,2740])-float(3.334*10/10000)

def power_function(x, w, d):
    return (xvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(x+d)/w))

poptx, pcov = curve_fit(power_function, myrange, xvalues,p0 = [0.9,-3.2])

print poptx, np.mean(myrange)

plt.figure()
plt.suptitle('Power as a Function of Knife Blade Displacement')
plt.title(r'$P(x)$')
plt.plot(myrange,xvalues,'rx')
plt.plot(np.arange(myrange[0],myrange[-1],0.01),power_function(np.arange(myrange[0],myrange[-1],0.01),poptx[0], poptx[1]))
plt.ylim((0,1))
plt.ylabel('Power (mW)')
plt.xlabel('Knife Displacement (mm)')
plt.show()
