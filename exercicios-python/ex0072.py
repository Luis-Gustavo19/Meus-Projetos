'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
tupla =('zero','um','dois','três','Quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
'''n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n >20:
    n = int(input('Digite um número entre 0 e 20: '))
for c in range(n,len(tupla)):
    print(f'Você digitou o número {n}, e ele por extenso é {tupla[c]} está na posição {c}')
    break
print(len(tupla))'''
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Digite um número entre o e 20: '))
print(f'Você digitou o número {tupla[n]}')
