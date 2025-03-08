# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = int(input('Digite um angulo: '))
print('O angulo {}, tem o seno {:.2f}, cosseno {:.2f}, e tangente {:.2f}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))