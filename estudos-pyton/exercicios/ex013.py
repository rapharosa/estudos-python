# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario = int(input('Qual seu salario? '))
novosalario = salario*1.15

print('Seu novo salario com o aumento é de RS{:.2f}'.format(novosalario))