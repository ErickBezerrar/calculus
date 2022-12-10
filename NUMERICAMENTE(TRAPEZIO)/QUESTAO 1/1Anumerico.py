import numpy as np
import math

a = 0.0
b = 1.0
N = 1000; 
x = np.linspace(a,b,N)
y=((2*x+1)/(5*x-1)**(1/2))
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))  #CRIA UMA LISTA COM CADA VALOR DE "X"
print(integral)