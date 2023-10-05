'''Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR'''
n = int(input('Digite o número: '))
resultado = n %2
if(resultado!= 0):
    print("O número é impar")
else:
    print('O número é par')

