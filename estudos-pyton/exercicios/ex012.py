# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
preco = float(input('Qual o preço original do produto? '))
d = preco * 0.05
np = preco - d

print('o desconto de 5 por cento de R${}, foi de R${:.2f} \n o produto com desconto ficou em R${:.2f}'.format(preco, d, np))