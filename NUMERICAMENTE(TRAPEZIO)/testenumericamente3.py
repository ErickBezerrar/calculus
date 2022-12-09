import numpy as np

a = 1.0
b = 5.0
N = 1000; 
h = (b-a)/N
x = np.linspace(a,b,N)
y=x**5; 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))
print(integral)