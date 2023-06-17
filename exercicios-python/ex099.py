'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def Maior(*num):
    maior = 0
    for v in num:
        if len(num) -1 ==0:
            maior = v
        elif v > maior:
            maior =v
    print(f'Você adicionou {len(num)} valores.'
          f' O maior valor encontrado foi {maior}')

Maior(2,9,4,5,7,1)
Maior(4,7,0)
Maior(1,2)
Maior(6)
Maior(0)