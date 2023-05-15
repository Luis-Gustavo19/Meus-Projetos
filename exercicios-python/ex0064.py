'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
digitos = 0
soma = 0
vcps = False
while not vcps:
    n = int(input('Digite um número [999 para parar]: '))
    soma = soma + n
    digitos = digitos + 1
    if(n == 999):
        vcps = True
        soma = soma - 999
        digitos = digitos - 1
        print('VOCê DIGITOU {} NÚMEROS E soma de todos os números deu o valor de {}'.format(digitos,soma))
