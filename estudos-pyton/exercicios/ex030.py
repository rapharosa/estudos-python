# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
numero = int(input('Digite um numero inteiro: '))

resposta = numero % 2
print('Seu numero é par'if resposta == 0 else 'seu numero é impar')