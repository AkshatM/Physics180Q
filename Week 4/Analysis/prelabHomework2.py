from OpticsCodes import Tmatrix,radius_of_curvature,waist_factor
from itertools import product
import numpy as np

desired_waist = pow(75*670e-9/(np.pi*pow(3,0.5)),0.5)

focal_length_list = [53,30,33,94,106,75,35,40] # in mm
propagation_distance = np.arange(0,100,1) # in mm
inverse_q_factor = -1j*670e-9/(np.pi*pow(desired_waist,2))
desired_inverse_q = -1j*670e-9/(np.pi*pow(2.79e-4,2))

print 'Inverse Q factor init: ' + str(inverse_q_factor)
print 'Desired Q factor waist: ' + str(waist_factor(desired_inverse_q))

focal_length_map = product(focal_length_list,focal_length_list)

def getKey(item):
    return np.sqrt(pow(item[2] - radius_of_curvature(desired_inverse_q),2)+pow(item[3]- waist_factor(desired_inverse_q),2))

L = []

for (x,y) in focal_length_map:
    d = x + y
    first_lens_constructor = '1, 0;'+ str(-1/float(x))+',1'
    prop_distance = '1,'+str(d)+';0,1' 
    second_lens_constructor = '1, 0;'+ str(-1/float(y))+',1'
    a = Tmatrix(first_lens_constructor)
    a.update_system(prop_distance,second_lens_constructor)
    new_q = a.new_quality_factor(inverse_q_factor)
    L.append((new_q, np.absolute(new_q - desired_inverse_q),radius_of_curvature(new_q),waist_factor(new_q),x,y,d))

for x in sorted(L, key=getKey):
    print x

        
        
