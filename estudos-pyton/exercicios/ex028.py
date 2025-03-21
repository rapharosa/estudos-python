#Escreva um programa que faça o computador pensar um numero inteiro entre 0 e 5 e peça para o usuario descobrir qual numero
#foi escolhido pelo computador. O programa deverá se o usuario venceu ou perdeu
import random
numero = random.randrange(0, 5)

resposta = int(input('Pensei em um numero de 0 a 5, advinhe qual foi... '))

print('Acertou miseravi' if numero == resposta else 'errrrrroooouuu')