# Faça um programa que leia a frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela ultima vez

frase = str(input('digite uma frase: ')).lower()
print('a frase escrita foi: {}'.format(frase))

print('na frase, a letra a aparece {} vezes'.format(frase.strip().count('a')+1))
print('e aparece a ultima vez na posição {}'.format(frase.strip().rfind('a')))