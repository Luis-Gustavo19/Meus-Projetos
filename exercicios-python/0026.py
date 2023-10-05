'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
fras = str(input('digite sua frase: ').lower()).strip()
print('a letra "a" aparece {} vezes na frase'.format(fras.count('a')))
print('a letra a apareceu na posição {}'.format(fras.find('a')+1))
print(' a ultima vez que a letra a aparece é na posição {} '.format(fras.rfind('a')+1))