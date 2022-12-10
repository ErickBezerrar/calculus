import numpy as np
import math
from sympy import*

a = 0.0
b = pi/2
N = 1000; 
x = np.linspace(a,b,N)
y=(sin(3*x))*(cos(x)); 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print(integral)