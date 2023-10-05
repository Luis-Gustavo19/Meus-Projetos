'''Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input('Digite om valor: '))
if(n1 > n2 and n1 >n3):
    print("O VALOR MAIOR INSERIDO É {} ".format(n1))
if(n2 > n1 and n2 > n3):
    print("O maior número é {}".format(n2))
if(n3 > n1 and n3 > n2):
    print("O Maior número é {} ".format(n3))
if(n1 <= n2 and n1 <=n3):
    print("O Menor Valor é {} ".format(n1))
if(n2 <= n3 and n2 <=n1):
    print('O menor valor é {} '.format(n2))
if(n3 <= n2 and n3 <= n1):
    print("O menor Valor é {} ".format(n3))