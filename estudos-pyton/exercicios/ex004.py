# Faça um programa que leia algo pelo teclado, e mostre na tela o seu tipo primitivo, e 
# todas as informações possiveis sobre ele

d = input('Digite algo: ')
print('o que foi digitado é do tipo ', type(d))
print('Só tem espaços? ', d.isspace())
print('É numerico? ', d.isnumeric())
print('É alfabetico? ', d.isalpha())
print('É alfanumerico? ', d.isalnum())
print('Está em maiusculas? ', d.isupper())
print('Está em minusculas? ', d.islower())
print('Está capitalizada? ', d.istitle())