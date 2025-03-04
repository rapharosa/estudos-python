# escreva um programa que leia um valor em metros o exiba convertido em centimetros e milimetros

m = int(input('digite o valor em metros '))
print('Esse valor é o mesmo que {}cm, e {}mm'.format(m*100, m*1000))