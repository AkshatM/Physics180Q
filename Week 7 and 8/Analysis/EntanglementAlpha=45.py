import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *
from scipy import stats

alpha = 45
beta = np.array(range(0,190,10)) - 7*np.ones(19)
coinc = np.array([9.84,13.94,17.92,21.16,22.52,23.26,22.88,21.7,18.22,15.08,
                  11.9,8.58,4.92,2.98,2.06,2.42,4.1,6.18,9.82])

def fit_function(beta,a,beta_c,V,P):
    return (a/2)*(1 - V*np.sin((np.pi/180)*((beta-beta_c)/P)))

popt, pcov = curve_fit(fit_function, beta, coinc)

print(popt,pcov)

plt.figure()
plt.plot(beta,coinc,'rx',label = 'Raw Data')
plt.plot(beta,fit_function(beta,popt[0],popt[1],popt[2],popt[3]), label = 'Fit')
plt.title(r'Coincidence Counts vs. $\beta$ for $\alpha = 45$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend()
plt.xlim([-10,180])
plt.show()
