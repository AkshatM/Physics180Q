import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = np.array([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5])
xvalues = float(3.334/10000)*np.array([17,31,181,399,772,1260,2000,2490,2730,2820,2840])-float(3.334*15/10000)

def power_function(x, w, d):
    return (xvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(x+d)/w))

myrange2 = np.array([0,0.25,0.5,0.75,1,1.25,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,2,2.25])
yvalues = float(3.334/10000)*np.array([0.4,0.4,1.7,7.7,37.3,231,623,933,1340,1770,2120,2350,2480,2600,2800,2820])-float(3.334*0.4/10000)

def power_function2(y, w, d):
    return (yvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(y+d)/w))

poptx, pcov = curve_fit(power_function, myrange, xvalues)
popty, pcov = curve_fit(power_function2, myrange2, yvalues)

print poptx, np.mean(myrange)
print popty, np.mean(myrange2)

plt.figure()
plt.suptitle('Power as a Function of Knife Blade Displacement - First Position')
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

