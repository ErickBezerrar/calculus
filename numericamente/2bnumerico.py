from math import *

def f(x):
    funcao = ((x+4)**(1/2))
    return funcao

def trapezio(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma

a = -1
b = 4
n = 100 #Número de subintervalos

result = trapezio(f, a, b, n)
print('Resultado numérico =', result)