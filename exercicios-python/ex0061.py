'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
#leia o primeiro termo
p1 = int(input('Digite o primeiro termo da PA: '))
#LEIA A RAZÃO
raz = int(input('Digite a razão da PA: '))
cont = 1
print(p1,end='')
while cont < 10:
    p1 = p1 + raz
    print('--⊳',end='')
    cont = cont + 1
    print(p1, end='')
print('--⊳ FIM')









