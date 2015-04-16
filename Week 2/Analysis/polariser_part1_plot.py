import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return pow(np.sin(2*t),2)

myrange = np.arange(0,370,10)
values = float(3.334/10000)*np.array([122,202,230,202,140,62,1.9,21,100,196,255,324,280,204,126,26,
          19,85,192,242,298,253,199,108,23,25,100,200,267,325,270,200,105,20,22,90,200])
yerr = float(3.334/10000)*np.array([1,1,1,1,2,2,0.3,3,3,1,3,3,4,1,3,4,1,5,1,2,3,1,1,3,3,2,2,2,2,2,2,1,4,4,2,2,1])

plt.figure(1)
plt.suptitle('Power Versus Angle - Third Polariser')
plt.subplot(121)
plt.errorbar(myrange, values, yerr=yerr, ecolor = 'r', linestyle= '--')
plt.xlim((0,360))
plt.ylabel('Power (mW)')
plt.xlabel('Angle (Degrees)')
plt.title('Power in Polariser')
plt.subplot(122)
plt.plot(myrange,f(np.radians(myrange)))
plt.xlabel('Angle (Degrees)')
plt.title(r'$\sin^{2}(2\theta)$')
plt.xlim((0,360))
plt.show()
