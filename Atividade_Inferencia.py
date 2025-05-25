#Ashton Apebio Mergulhão Segnibo, Nº USP: 15441765

import math
import numpy as np

file =r"AMOSTRA_3"

with open(file) as amostra:
    dados = amostra.read().split()

for i in range(100):
    try:
        dados[i] = int(dados[i])
    except IndexError:
        break


u = sum(dados)/len(dados) # u = 4.3625

def encontrar_parametro(x):
    return x + u*np.exp(-x) - u

def bissecao(a,b):
    c = np.mean(a+b)
    while abs(a-b) > 0.00001:
        if encontrar_parametro(a) * encontrar_parametro(b) < 0:
            if encontrar_parametro(c) * encontrar_parametro(a) < 0:
                b = c
            elif encontrar_parametro(c) * encontrar_parametro(b) < 0:
                a=c
        c = (a+b)/2
    return c
        
x_0 = min(dados)
x_1 = max(dados)
EMV = round(bissecao(x_0,x_1),5)

print(f'a) O valor da estimativa de máxima verossimilhança é {EMV}\n')

#--------------------------------------------------------------------

def zero_truncated_poisson(x,p):
    return (math.e ** (-p)) * (p ** x) / (math.factorial(x) * (1 - math.e ** (-p)))

freq_observada = {}
freq_esperada = {}

for valor in dados:
    if valor in freq_observada:
        freq_observada[valor] += 1
    else:
        freq_observada[valor] = 1

freq_observada = dict(sorted(freq_observada.items()))
print(f'b)\n{'x':^10}|{'Freq. Observada':^17}|{'Freq. Esperada':^17}|{'f(x)':^10}')

p= 4.30352 #EMV
for x in freq_observada:
    freq_esperada[x] = zero_truncated_poisson(x, p)
    print(f'{x:^10}|{freq_observada[x]:^17}|{freq_esperada[x]*80:^17.2f}|{freq_esperada[x]:^10.3f}')

#--------------------------------------------------------------------

def esperanca(p):
    return p/(1-np.exp(-p))

def variancia(p):
    return esperanca(p) * (1 + p*(1 - 1/(1-np.exp(-p))))

p = 4.30352

E = esperanca(4.30352)
Var = variancia(4.30352)

print(f'c) E(X) = {E} e Var(X) = {Var}')
