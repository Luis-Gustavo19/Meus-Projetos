'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
 você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Brasil','Mexico','Paraguai','Luxemburgo','x')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ',end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l,end='')
