# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo"
cidade = str(input('Digite o nome de uma cidade: '))

tratada = cidade[:5].title().strip()

print('Santo' in tratada)