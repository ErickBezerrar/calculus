import numpy as np
import math
import matplotlib.pyplot as plt

lista_temperatura = [75.3, 77, 83.2, 84.8, 86.5, 86.4, 81.1, 78.6]

def funcao(x):
    funcao = x/8
    return funcao


def metodo_trapezio(f,a, b, N):
    h = ((b+1)-a)
    soma = 0
    for k in range(0, h):
        soma += lista_temperatura[k]
    return f(soma)

a = 9
b = 16
N = 8

def simpson(f,a,b):
    
    return

valor = metodo_trapezio(funcao, a, b, N)
print(valor)
lista_hora = [9, 10, 11, 12, 13, 14, 15, 16]

x=10
ax = plt.axes() 
ax.set_facecolor("#490a3d") 
plt.plot(lista_hora, lista_temperatura, color='#bd1550', label='TEMPERATURAS AO LONGO DO DIA',marker='o')
plt.plot(x, valor, color='#f8ca00', label='MÉDIA DAS TEMPERATURAS', marker='x')
plt.ylabel('Tem/Fahrenheit')
plt.xlabel('Horas')
plt.axis(ymin=50,ymax=120)
plt.axis(xmin=9,xmax=16)
plt.grid(True, color='white')
plt.legend()
plt.show()