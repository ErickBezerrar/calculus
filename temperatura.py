import matplotlib.pyplot as plt
import numpy as np
import math

lista_temperatura = [75.3, 77, 83.2, 84.8, 86.5, 86.4, 81.1, 78.6]

def funcao(x): 
    funcao = x/8
    return funcao


def trapz(f,a, b, N):
    h = ((b+1)-a)
    soma = 0
    for k in range(0, h):
        soma += lista_temperatura[k]
    return f(soma)

a = 9
b = 16
N = 8

resultado = trapz(funcao, a, b, N)
print(resultado)
lista_hora = [9, 10, 11, 12, 13, 14, 15, 16]

x=10
ax = plt.axes() 
ax.set_facecolor("#490a3d") 
plt.plot(lista_hora, lista_temperatura,label='TEMPERATURAS AO LONGO DO DIA', color='#bd1550',marker='o')
plt.plot(x, resultado, label='MÉDIA DAS TEMPERATURAS',color='#f8ca00', marker='o')
plt.ylabel('Tem/Fahrenheit')
plt.xlabel('Horas')
plt.axis(ymin=50,ymax=120)
plt.axis(xmin=9,xmax=16)
plt.title('Temperaturas(9AM/16PM)')
plt.legend()
plt.grid(True)
plt.show()