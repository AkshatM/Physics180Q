import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *

# with filters

translation_stage_dist = (50/60)*(np.array([x for x in range(-20,85,5)]))-(50/60)*25 # in micrometers
coincidence_counts = np.array([14.08,13.3,12.64,12.6,11.74,11,10.9,
                               11.22,10.3,9.82,10.54,9.34,11.52,11.3,
                               12.68,12.66,13.72,14.04,14.42,14.54,14.86])
error = np.array([0.766,0.848,0.456,0.851,0.416,1.095,0.916,
                  1.731,1.072,0.798,1.018,0.723,0.855,0.346,
                  0.791,0.939,1.663,0.838,0.762,1.225,1.105])

def inverted_gaussian(l,k,c,t,r,x):
    return c*(t+r)*(1 - (2*((np.sqrt(r*t))/(t+r))*np.exp(-1*pow(k,2)*pow(l-((50/60)*x),2)/2)))

popt,pcov = curve_fit(inverted_gaussian,translation_stage_dist,coincidence_counts,p0 = [0.003,15.8,0.8,0.2,25],
                      sigma = error)

print(popt, popt[2] + popt[3])

test = (50/60)*np.array([x for x in range(-100,100)])

plt.figure()
plt.errorbar(translation_stage_dist,coincidence_counts,yerr = error, fmt = 'ro')
plt.plot(test,inverted_gaussian(test,popt[0],popt[1],popt[2],popt[3],popt[4]),'b')
plt.ylabel('Coincidence Counts s$^{-1}$')
plt.xlabel('Path difference (microns)')
plt.show()



