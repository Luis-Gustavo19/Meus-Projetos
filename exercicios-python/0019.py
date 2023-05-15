'''Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.'''
'''Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
#função choice pode sortear um nome na lista aleatório
#lista no python é representadas por cochetes[]
import random
a1 = str(input("digte o nome do primeiro aluno:"))
a2 = str(input("digite o nome do segundo aluno:"))
a3 = str(input("digite o nome do terceiro aluno: "))
a4 = str(input('digite o nome do seu quarto aluno: '))
sorteado = random.choice([a1,a2,a3,a4])
print(" o sorteado da vez foi: {}".format(sorteado))
