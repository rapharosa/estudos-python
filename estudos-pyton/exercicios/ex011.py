# Faça um programa que leia a largura e altura da parede em metros, calcule a sua area e a quantidade de tinta necessaria para 
# pinta-la, considere que cada litro de tinta pinta uma area de 2m²

print('Calculadora de gasto de tinta')
l = int(input('Qual largura da sua parede? '))
a = int(input('e qual a altura? '))
area = l * a
print('Sua parede tem uma area de {}m², e é necessario {} litros de tinta para pinta-la'.format(area, area/2))