# Escreva um programa que pergunte o salario de um funcionario e calcule seu valor com aumento
# Para salarios a R$1250,00 calcule aumento de 10%
# Para salarios inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o valor do salario '))

if salario > 1250:
    print('O novo salario é de {}'.format(salario * 1.1))
else:
    print('O novo salario é de {}'.format(salario * 1.15))

