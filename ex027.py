# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome, mostrando separadamente
nome = str(input('Digite seu nome completo: ')).strip()
ns= nome.split()
print('Olá, {} {}'.format(ns[0], ns[len(ns)-1]))