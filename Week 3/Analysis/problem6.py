import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit
import numpy as np

myrange = np.array([4,4.15,4.25,4.3,4.35,4.4,4.45,4.5,4.6,4.75,5])
xvalues = float(3.334/10000)*np.array([28,269,730,1040,1340,1650,1930,2150,2440,2600,2600])-float(3.334*15/10000)

def power_function(x, w, d):
    return (xvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(x+d)/w))

myrange2 = np.sort(np.array([2.5,2.75,2.7,2.65,2.8,2.85,2.9,3,2.6,2.78,2.82]))
yvalues = np.sort(float(3.334/10000)*np.array([16,983,418,188,1730,2250,2460,2580,77,1350,1920]))-float(3.334*0.4/10000)

def power_function2(y, w, d):
    return (yvalues[-1]/2.00)*(1 + erf(pow(2,0.5)*(y+d)/w))

poptx, pcov = curve_fit(power_function, myrange, xvalues, p0=[100,100])
popty, pcov = curve_fit(power_function2, myrange2, yvalues,  p0=[100,2.75])

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
