'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.'''
numero = int(input("Digite um número para ver sua tabuada: ".strip()))
for c in range(0,11):
    tabu = numero * c
    print( '\033[0;36m[',numero,'x',c,'=',tabu,']')


