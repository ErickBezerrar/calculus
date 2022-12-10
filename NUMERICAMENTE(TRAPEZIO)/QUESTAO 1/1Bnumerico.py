import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import*


a = 1.0
b = 2.0
N = 1000; 
x = np.linspace(a,b,N)
y=(1/(x*(x+1)**2)); 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print(integral)