import numpy
import cmath

def radius_of_curvature(inverse_q):
    ''' Returns the radius of curvature from an existing quality factor 1/q, denoted by inverse_q here'''
    return 1.00/inverse_q.real

def waist_factor(inverse_q, wavelength=635e-9, index = 1):
    ''' Returns the waist of a beam from an existing quality factor 1/q, denoted by inverse_q here. 
    Default options for wavelength and index of refraction are specified.'''
    return cmath.sqrt((-wavelength/(index*numpy.pi*inverse_q.imag)))

class Tmatrix: #for purely numeric computation

    def __init__(self,system_constructor='1,0;0,1'):
        ''' Constructs a Tmatrix. If you feed in no arguments, it assumes it's a 2D identity matrix'''
        self.tmatrix = numpy.matrix(system_constructor)

    def update_system(self, new_matrix_constructor, *args):
        ''' Updates the system - just feed in the strings corresponding to the matrices in your system in the order they appear '''
        self.tmatrix = (numpy.matrix(new_matrix_constructor))*(self.tmatrix)
        for strings in args:
            self.update_system(strings)

    def invert_system(self, invert_matrix_constructor):
        self.tmatrix = (numpy.linalg.inv(numpy.matrix(invert_matrix_constructor)))*(self.tmatrix)
    
    def new_quality_factor(self,inverse_q):
        ''' Returns the quality factor of a beam with initial inverted quality factor inverse_q after it passes through our system'''
        return (self.tmatrix[1,0] + self.tmatrix[1,1]*(inverse_q))/(self.tmatrix[0,0] + self.tmatrix[0,1]*(inverse_q))
        
        
