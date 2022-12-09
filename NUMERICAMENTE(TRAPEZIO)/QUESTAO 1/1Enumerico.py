import numpy as np
import math
from sympy import*

a = 0.0
b = 2.0
N = 1000; 
h = (b-a)/N
x = np.linspace(a,b,N)
y=((3*x+5)**(1/2)); 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print(integral)