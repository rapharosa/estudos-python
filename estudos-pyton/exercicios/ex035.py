# Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triangulo

reta1 = float(input('Digite o valor de um seguimento '))
reta2 = float(input('Agora mais um '))
reta3 = float(input('E o ultimo '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2 :
    print('As retas acima PODEM formar um triangulo')
else:
    print('As retas acima NÃO podem formar um triangulo')