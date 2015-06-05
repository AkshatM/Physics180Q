import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *

# without filters

translation_stage_dist = (50/60)*np.array([10,15,20,25,30,35,40,45,50,55,60,80,120]) -(50/60)*50
coincidence_counts = np.array([6.2,6.28,6,5.26,4.78,5.14,5.34,4.94,4.5,5.2,4.74,5.2,5.64])
error = np.array([0.3937,1.18,0.982,0.357,0.228,0.487,0.730,0.409,0.591,0.543,0.594,0.484,0.841])

def inverted_gaussian(l,k,c,t,r,x):
    return c*(t+r)*(1 - 2*((np.sqrt(r*t))/(t+r))*np.exp(-1*pow(k,2)*pow(l-(50/60)*x,2)/2))

popt,pcov = curve_fit(inverted_gaussian,translation_stage_dist,coincidence_counts, p0 = [0.1,6,0.8,0.2,0],
                      sigma = error)

print(popt, popt[2] + popt[3])

test = (50/60)*np.array([x for x in range(-100,100)])

plt.figure()
plt.errorbar(translation_stage_dist,coincidence_counts,yerr = error, fmt = 'ro')
plt.plot(test,inverted_gaussian(test,popt[0],popt[1],popt[2],popt[3],popt[4]),'b')
plt.ylabel('Coincidence Counts s$^{-1}$')
plt.xlabel('Path difference (microns)')
plt.show()
