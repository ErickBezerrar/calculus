import numpy as np
import math

a = 0.0
b = 3.141592653/2
N = 1000; 
x = np.linspace(a,b,N)
y=(np.sin(3*x))*(np.cos(x)); 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print(integral)