# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Sua viagem foi de quantos KM? '))

if km <= 200:
    preco = km * 0.5
    print('Sua viagem custou R${:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('Sua viage custou R${:.2f}'.format(preco))