# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input('Velocidade registrada: '))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Velocidade acima do permitido, você foi multado em R${},00'.format(multa))
else:
    print('Velocidade dentro do permitido')