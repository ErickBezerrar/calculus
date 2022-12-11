import numpy as np
import math

a = 1.0
b = 5.0
N = 1000;

x = np.linspace(a,b,N) #Array de 1000 elementos de 1 até 5
print((len(x)))
print(x)

y=(x**5) #Função f(x)

integral = 0.0
for k in range(len(x) - 1): #K é 0 no momento inicial

    integral +=0.5*(x[k+1]-x[k])*(y[k+1]+y[k]) #a cada iteração a integral soma o valor anterior com o obtido integral = integral + integral
print("O valor aproximado da integral: ", integral) 


#0.5*(1.004004 - 1) * (x**5)[1] + (x**5)[0]
#meio1/2 vezes k + 1(que seria o meu 1, primeiro valor do array) 