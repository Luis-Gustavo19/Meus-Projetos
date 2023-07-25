'''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
from time import sleep
print("Vou pensar em um número de 0 a 5 tente adivinhar")
n1 = random.randint(0,5)
usuario = int(input("Em qual número eu pensei ? "))
sleep(4)
if(n1==usuario):
    print("PARABÉNS,VOCÊ ACERTOU. O NÚMERO QUE PENSEI FOI {}".format(n1))
else:
    print('Você errou.O número escolhido foi {}'.format(n1))
