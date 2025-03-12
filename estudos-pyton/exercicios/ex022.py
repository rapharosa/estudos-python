# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem ao todo, sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
junto = nome.split()
resultadojunto = ''.join(junto)
print(len(resultadojunto))
print(len(junto[0]))