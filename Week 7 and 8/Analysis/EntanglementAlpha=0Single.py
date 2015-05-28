import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

alpha = 0
beta = np.array(range(0,190,10)) - 7*np.ones(19)
single = np.array([6570.92,6594.76,6567.84,6575.14,6567.64,6595.02,6585.82,
                   6602,6599.4,6607.56,6605.98,6605.96,6597.18,6589.94,6589.42,
                   6620.2,6587.36,6590.68,6594.64])

slope,intercept,r_value, p_value, std_err = stats.linregress(beta,single)

print(r_value**2,slope,intercept)

plt.figure(1)
plt.subplot(121)
plt.plot(beta,single,'rx',label = 'Raw Data')
plt.plot(beta,slope*beta + intercept,label = 'Best Fit')
plt.title(r'Single Counts vs. $\beta$ for $\alpha = 0$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend(loc='lower right')
plt.xlim([-10,180])
plt.subplot(122)
plt.plot(beta,single,'rx',label = 'Raw Data')
plt.text(2,6100,'Slope = ' + str(slope), fontsize=12)
plt.text(2,6050,r'$R^{2}$ = ' + str(r_value**2), fontsize=12)
plt.plot(beta,slope*beta + intercept,label = 'Best Fit')
plt.title(r'Single Counts vs. $\beta$ for $\alpha = 0$')
plt.xlabel(r'$\beta$ (in degrees)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.legend(loc='lower right')
plt.xlim([-10,180])
plt.ylim([6000,7000])
plt.show()
