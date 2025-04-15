# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
primeiro = int(input('Digite um numero '))
segundo = int(input('mais um '))
terceiro = int(input('agora o ultimo '))

menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro 

maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))