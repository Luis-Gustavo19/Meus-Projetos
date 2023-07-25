'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso
, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
import random
#gerar números alatórios e colocar em uma tupla
cont = 0
while cont < 5:
    cont += 1
    sort = random.randint(0,100)
    if cont == 1:
        a = sort
    elif cont == 2:
        b = sort
    elif cont == 3:
        c = sort
    elif cont == 4:
        d = sort
    else:
        e = cont
tupla  =(a,b,c,d,e)
# LISTAGEM DE NÚMEROS GERADOS E MAIOR E MENOR VALOR DA TUPLA
print('-=-' * 20)
print('AQUI ESTÃO TODOS OS NÚEMROS QUE ESTÃO NA TUPLA: ')
for c in tupla:
    print(c,end=' ')
    print(' ', end='' )
print('')
print('-=-' * 20)
print('O maior número da tupla é: ', end='')
print(max(tupla))
print('-=-' * 20)
print('O menor da número da tupla é: ',end ='')
print(min(tupla))
print('-=-' * 20)