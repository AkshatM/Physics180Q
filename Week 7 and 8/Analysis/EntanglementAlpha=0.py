import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *
from scipy import stats

alpha = 0
beta = np.array(range(0,190,10)) - 7*np.ones(19)
coinc = np.array([1.22,1.06,1.72,4.18,6.2,9.46,11.92,15.06,17.92,18.22,19.6,
                  18.66,15.98,13.78,10.72,7.183,4.84,2.38,1.14])

def fit_function(beta,a,beta_c,V,P):
    return (a/2)*(1 - V*np.sin((np.pi/180)*((beta-beta_c)/P)))

popt, pcov = curve_fit(fit_function, beta, coinc)

print(popt,pcov)

plt.figure()
plt.plot(beta,coinc,'rx',label = 'Raw Data')
plt.plot(beta,fit_function(beta,popt[0],popt[1],popt[2],popt[3]), label = 'Fit')
plt.title(r'Coincidence Counts vs. $\beta$ for $\alpha = 0$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend()
plt.xlim([-10,180])
plt.show()
