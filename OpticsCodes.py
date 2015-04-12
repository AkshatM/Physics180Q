import numpy
import cmath

def radius_of_curvature(q):
    return 1/q.real

def waist_factor(q, wavelength=635e-9, index = 1):
    return cmath.sqrt(-index*numpy.pi*q.imag/(wavelength))

class Tmatrix:

    def __init__(self,system_constructor='1,0;0,1'):
        self.tmatrix = numpy.matrix(system_constructor)

    def update_system(self, new_matrix_constructor, *args):
        self.tmatrix = (self.tmatrix)*(numpy.matrix(new_matrix_constructor))
        for strings in args:
            self.update_system(strings)
        
    def new_quality_factor(self,inverse_q):
        # remember to feed in 1/q - it is treated as a complex number here
        return (self.tmatrix[1,0] + self.tmatrix[1,1]*(inverse_q))/(self.tmatrix[0,0] + self.tmatrix[0,1]*(inverse_q))

        
        
        
