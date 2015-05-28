import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

alpha = 45
beta = np.array(range(0,190,10)) - 7*np.ones(19)
single = np.array([6496.74,6510.08,6538.96,6547.66,6536.56,6552.86,
                   6560.52,6540.9,6511.88,6528.94,6544.08,6493.34,
                   6490.14,6506.04,6513.32,6488.44,6468.72,6507.6,
                   6476.6])

slope,intercept,r_value, p_value, std_err = stats.linregress(beta,single)

print(r_value**2,slope,intercept)

plt.figure(1)
plt.subplot(121)
plt.plot(beta,single,'rx',label = 'Raw Data')
plt.plot(beta,slope*beta + intercept,label = 'Best Fit')
plt.title(r'Single Counts vs. $\beta$ for $\alpha = 45$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend(loc='lower right')
plt.xlim([-10,180])
plt.subplot(122)
plt.plot(beta,single,'rx',label = 'Raw Data')
plt.text(2,6100,'Slope = ' + str(slope), fontsize=12)
plt.text(2,6050,r'$R^{2}$ = ' + str(r_value**2), fontsize=12)
plt.plot(beta,slope*beta + intercept,label = 'Best Fit')
plt.title(r'Single Counts vs. $\beta$ for $\alpha = 45$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend(loc='lower right')
plt.xlim([-10,180])
plt.ylim([6000,7000])
plt.show()
