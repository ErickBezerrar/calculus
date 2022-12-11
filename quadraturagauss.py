import numpy as np
import math

a = 0
b = 4
N = 4; 
x = np.linspace(a,b,N)
y=((16-x**2)**(1/2))
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print("Area do primeiro quadrante:", integral)

print("Area total aproximada:", integral * 4)