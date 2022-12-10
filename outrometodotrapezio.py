import math


def funcao(x):
    return (x**5)


def metodo_trapezio(f,a, b, N):
    h = (b-a)/N
    soma = 0                        
    for k in range(1, N):               
        soma += f(a + k * h)           
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

a = 1
b = 5
N = 1000

r = metodo_trapezio(funcao,a,b,N)
print(r)
