import numpy as np
from scipy.optimize import *
import matplotlib.pyplot as plt

zvalue = np.array([113,392,780]) # in mm
waists = np.array([0.277,0.195,0.6]) #in mm
wavelength = 670e-06 #in mm

def waist(z,w0,d):
    return pow(w0,2)*(1 + pow(((z+d)*wavelength/(np.pi*pow(w0,2))),2))

popt,pcov = curve_fit(waist,zvalue,waists*waists)

print np.min(waist(np.arange(0,2000,1),popt[0],popt[1]))

print np.where(waist(np.arange(0,2000,1),popt[0],popt[1]) == np.min(waist(np.arange(0,2000,1),popt[0],popt[1])))
plt.figure()
plt.title('Waist Profile')
plt.plot(np.arange(0,2000,1),waist(np.arange(0,2000,1),popt[0],popt[1]))
plt.plot(zvalue,waists,'rx')
plt.ylabel(r'w(z)$^{2}$')
plt.xlabel(r'z (in mm)')
plt.show()
