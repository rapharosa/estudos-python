# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem ao todo, sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print('Seu nome maiusculo {}'.format(nome.upper()))
print('Seu nome minusculo {}'.format(nome.lower()))
junto = nome.split()
resultadojunto = ''.join(junto)
print('Seu nome ao todo tem {} letras'.format(len(resultadojunto)))
print('Seu primeiro nome tem {} letras'.format(len(junto[0])))