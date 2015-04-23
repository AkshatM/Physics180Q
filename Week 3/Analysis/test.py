from OpticsCodes import *
import numpy
import matplotlib.pyplot as plt

inverse_foclength = -1.00/(30e-03)
total_distance = 500

a = Tmatrix('1,0;'+str(inverse_foclength)+',1')
inverse_q = 0 - 1j*(635e-9)/(numpy.pi*3)
radius_descriptor1 = [0 for x in xrange(0,total_distance + 1)]
waist_descriptor1 = [0 for x in xrange(0,total_distance + 1)]

for x in xrange(0,total_distance + 1):
    b = Tmatrix('1-'+str(x*inverse_foclength*pow(10,-3))+','+str(x*pow(10,-3))+';'+str(inverse_foclength)+',1')
    newq1 = b.new_quality_factor(inverse_q)
    radius_descriptor1[x] = radius_of_curvature(newq1)
    waist_descriptor1[x] = waist_factor(newq1)

plt.figure()
plt.plot(numpy.arange(0,total_distance + 1),numpy.array(radius_descriptor1))
plt.plot(numpy.arange(0,total_distance + 1),numpy.array(waist_descriptor1),'r--')
plt.xlabel('Distance (mm)')
plt.ylabel('Beam Waist (Red); Radius of Curvature (Blue)')
plt.title('Evolution of Beam Along z')
plt.show()
