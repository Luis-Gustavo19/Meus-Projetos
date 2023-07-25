'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
crt = False
while not crt:
    opcao = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Qual operação deseja realizar: '''))
    if(opcao >5):
        print('Digito inválido')
    elif(opcao <1):
        print('Digito inválido')
    elif(opcao == 4):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('novos valores cadastrados')
    elif(opcao == 1):
        soma = n1 + n2
        print('A SOMA DO NUMERO {} E DO NÚMERO {} É {}'.format(n1,n2,soma))
    elif( opcao == 2):
        multi = n1 * n2
        print('A MULTIPLUICAÇÃO DO NÚMERO {} E DO NÚMERO {} É {}'.format(n1,n2,multi))
    elif( opcao == 3):
        if(n1 > n2):
            print('O NÚMERO {} É MAIOR QUE O NÚMERO {}'.format(n1,n2))
        else:
            print('O NÚMERO {} É MAIOR QUE O NÚMERO {}'.format(n2,n1))
    elif(opcao == 5):
        crt = True
        print('encerrando...')
        sleep(5)
print('Programa encerrado =')




