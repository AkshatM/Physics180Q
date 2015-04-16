# Description

Some code I wrote to be able to do simple optical ray-tracing calculations for Physics 180Q. This code also houses the content of my writing for Physics 180Q, where we work on quantum optics and write lab reports summarising our results. 

# OpticsCodes.py
- Defines a class `Tmatrix` that consists of a matrix representation of my system. This system can be updated to reflect additional complexity. _To be be added: a simplifying function that can remove the additional complexity if needed._
- Defines functions for calculating the minimum beam waist and radius of curvature of a Gaussian laser beam.

# Important Notes

- A `Tmatrix` object is initialised with strings. For instance, to obtain the identity matrix, simply feed in '1,0;0,1' as an argument to the `Tmatrix` class.
- The `update_system` function argument can be used to multiply in as many matrix elements as needed (in other words, it takes a variable number of arguments); however, care should be taken to feed in the matrices in the right order. For instance, `update_system('1,2;2,1','2,3;3,1')` will first multiply '1,2;2,1' with the existing system, and then multiply '2,3:3,1' with the newly updated system.
