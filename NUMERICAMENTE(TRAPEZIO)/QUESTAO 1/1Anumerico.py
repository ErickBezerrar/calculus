import numpy as np
import math
from sympy import*

r = Symbol('r')
resolveraiz = sqrt(5*r-1)

a = 0.0
b = 1.0
N = 10000; 
x = np.linspace(a,b,N)
y=((2*x+1)/2); 
integral = 0.0
for k in range(len(x) - 1):
    integral +=0.5*((x[k+1]-x[k])*(y[k+1]+y[k]))  #CRIA UMA LISTA COM CADA VALOR DE "X"
print(integral)