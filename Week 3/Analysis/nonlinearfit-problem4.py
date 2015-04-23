import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import sqrt,pi

z0 = np.array([50,381+50,(2*381)+50])
wx = np.array([0.87705473,0.67974084,0.51774747])
wy = np.array([0.29942251,0.26987042,0.2580873])

def waist_function(z, w0, d):
    return pow(w0,2)*(1 + pow((z + d)/(pi*pow(w0,2)/635e-9), 2))

poptx,pcovx = curve_fit(waist_function, z0, ydata = wx*wx, p0 = np.array([1,-735]))
popty,pcovy = curve_fit(waist_function, z0, ydata = wy*wy)

print poptx
print popty

plt.figure()
plt.suptitle('Waist Sizes as a Function of Distance')
plt.subplot(121)
plt.title('$w_{x}$')
plt.plot(z0,waist_function(z0, poptx[0], poptx[1]))
plt.plot(z0,wx*wx,'rx')
plt.ylim((0,1))
plt.ylabel('Waist Sizes (mm)')
plt.xlabel('Distance (mm)')
plt.subplot(122)
plt.title('$w_{y}$')
plt.plot(z0,waist_function(z0, popty[0], popty[1]))
plt.plot(z0,wy*wy,'rx')
plt.ylim((0,1))
plt.ylabel('Waist Sizes (mm)')
plt.xlabel('Distance (mm)')
plt.show()
