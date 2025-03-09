# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre
# o comprimento da hipotenuza
import math
adjacente = float(input('Informe o cateto adjacente: '))
oposto = float(input('Informe o cateto oposto: '))
hipotenuza = math.hypot(adjacente, oposto)
print('a hipotenuza é: {:.2f}'.format(hipotenuza))