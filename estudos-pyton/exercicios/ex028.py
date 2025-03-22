#Escreva um programa que faça o computador pensar um numero inteiro entre 0 e 5 e peça para o usuario descobrir qual numero
#foi escolhido pelo computador. O programa deverá se o usuario venceu ou perdeu
import random
from time import sleep
numero = random.randrange(0, 5)

print('Vou pensar em um numero...')
sleep(2)
resposta = int(input('Advinhe qual foi... '))

print('Acertou miseravi' if numero == resposta else 'errrrrroooouuu')