'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
#entendi PORRRAA!!! NENHUMAAAAAA
n = int(input("Digite um número: "))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end ='')
        tot = tot + 1
    else:
        print(c,'\033[36m'.format(c))
if tot > 2:
    print("O número {} NÃO é primo, pois foi dividido {} vezes".format(n,tot))
else:
    print("O número é primo,pois só foi dividido {} vezes".format(tot))
