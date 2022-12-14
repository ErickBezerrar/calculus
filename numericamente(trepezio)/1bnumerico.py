from math import *

def f(x):
    funcao = 1/(x*(x+1)**2)
    return funcao

def trapezio(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma

a = 1
b = 2
n = 1000

result = trapezio(f, a, b, n)
print('Resultado numérico =', result)