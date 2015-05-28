import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

currents = np.array([25.90,27.80,29.70,31.80,33.9,36,38]) # in mA
power = ((20-0)/(currents[-1]-currents[0]))*(currents- currents[0]) # in mW

print(power)

coincidence_counts = np.array([1.22,7.28,14.98,24.26,29.5,38.68,42.6])
# in counts per second

slope,intercept,r_value, p_value, std_err = stats.linregress(power,coincidence_counts)

print(r_value**2,slope,intercept)

plt.figure()
plt.plot(power,coincidence_counts,'rx',label = 'Raw Data')
plt.plot(power,slope*power + intercept,label = 'Best Fit')
plt.title('Coincidence Counts vs. Laser Pump Power')
plt.xlabel('Power (in mW)')
plt.ylabel(r'Counts (in $s^{-1}$)')
plt.show()

