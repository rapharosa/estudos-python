# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
# Ex: digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um numero com ponto '))
res = math.floor(num)

print('A parte inteira de {}, é {}'.format(num, res))