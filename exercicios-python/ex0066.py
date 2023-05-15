'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
 digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
 e qual foi a soma entre elas (desconsiderando o flag).'''
cont = 0
s = 0
while True:
    n = int(input('Digite um númeor inteiro: '))
    if(n == 999):
        break
    s = s + n
    cont = cont + 1
print(f'Você digitou {cont} valores e o total deu {s}')