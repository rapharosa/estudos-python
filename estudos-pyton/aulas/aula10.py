nome = str(input('Qual seu nome? '))
if nome == 'Raphael':
    print('Belo nome!')
print('Olá, {}'.format(nome))

#outra forma de escrever o mesmo codigo acima
print('caraca' if nome == 'Raphael' else 'tendi')