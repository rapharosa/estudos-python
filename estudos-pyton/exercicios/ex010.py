# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# considere 1 dolar 3,27 reais

n = int (input('Quantos reais você tem? '))
print('Com esse valor você consegue comprar {:.2f} dolares'.format(n/3.27))