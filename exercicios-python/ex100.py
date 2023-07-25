'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai
colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
import random

def Sortear_numero(lista):
    for c in range(1,6):
        lista.append(random.randint(1,10))

    print(f'Os valoes sorteados foram {lista}')


def SomaPar(lista):
    maior_par=[]
    for c in lista:
        if c % 2 ==0:
            maior_par.append(c)
    print(f'Dos {len(lista)} elementos na lista. A soma dos valores pares é: {sum(maior_par)}')


numeros=[]
Sortear_numero(numeros)
SomaPar(numeros)
