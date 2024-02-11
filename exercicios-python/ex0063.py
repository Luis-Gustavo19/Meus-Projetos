'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
 e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0- 1 – 1 – 2 – 3 – 5 – 8
'''
n = int(input('Quantos termos você quer mostrar:  '))
cont = 0
g = 0
g2 = 1
g3 = 1
if n >0:
    if n == 1:
        print(g)
    elif n ==2:
        print(g)
        print(g2)
    elif(n==3):
        print(g)
        print(g2)
        print(g3)
    else:
        print(g)
        print(g2)
        print(g3)
        while cont < n - 3:
            g4 = g3 + g2
            g2 = g3
            g3 = g4
            cont = cont + 1
            print(g4)
print('FIM')
