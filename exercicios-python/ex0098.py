'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1             b) de 10 até 0, de 2 em 2       c) uma contagem personalizada'''
from time import sleep
def Contador(inicio,fim,passo):
    dez = 10
    print('-='*30)
    while dez != 0 or dez <0:
        print(dez,end='  ')
        sleep(0.1)
        dez-=1

    if dez == 0:
        print(dez)
    print('')
    print('-='*30)
    #fazer de 10 até 0 de dois em dois
    dez2 =10
    while dez2 != 0:
        print(dez2,end='  ')
        sleep(0.1)
        dez2-=2
    if dez == 0:
        print(dez)
    print('')
    print('-='*30)
    print(f'Sua Vez! Vamos Personalizar sua contagem!Inicio:{inicio},Fim:{fim},Passo:{passo}')
    while inicio != fim:
        if fim > inicio:
            print(inicio,end=' ')
            inicio += passo
            if inicio >fim:
                break
            if inicio == fim:
                print(inicio)

        else:
            print(inicio,end=' ')
            inicio -=passo
            if inicio < fim:
                break
            if inicio == fim:
                print(inicio)
    print('')
    print('-='*30)

inicio = int(input('Digite o valor de início: '))
fim = (int(input('Digite o número final: ')))
passo = abs(int(input('Digite o passo que deseja: ')))
if passo ==0:
    passo =1
Contador(inicio,fim,passo)