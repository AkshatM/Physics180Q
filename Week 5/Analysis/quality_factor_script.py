from OpticsCodes import *
import numpy as np

min_waist = 0.24 # in mm
d = 680 # in mm
wavelength = 670e-6 # in mm
fe = 30 # mm
fo = 53 # mm

def waist(z):
    return np.sqrt(pow(min_waist,2)*(1 + pow(((z-d)*wavelength/(np.pi*pow(min_waist,2))),2)))

def radius(z):
    return pow(z,2)*(1 + pow((np.pi*pow(min_waist,2)/(wavelength*(z-d))),2))

def quality_factor(z):
    return (1/radius(z) - 1j*(wavelength/(np.pi*waist(z)*waist(z))))

init_quality_factor = quality_factor(100)

a = Tmatrix()
a.update_system('1,0;'+str(fo)+',1','1,0;'+str(fe+fo)+',1','1,0;'+str(fe)+',1','1,'+str(670-100-fe-fo)+';0,1')
invert_new_quality_factor = a.new_quality_factor(1.00/init_quality_factor)

print(waist_factor(invert_new_quality_factor))
print(radius_of_curvature(invert_new_quality_factor))
