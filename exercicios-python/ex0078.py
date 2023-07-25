'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
#adicionando números na lista
lista = []
contmaior = 0
contmenor = 0
for add in range(0,5):
     lista.append(int(input(f'Digite um valor para a posição {add}: ')))
pos = p =0
print(lista)
print('=-=' * 20)

#MOSTRANDO MAIOR VALOR
for p,v in enumerate(lista):
 if v== max(lista) and contmaior == 0:
     print(f'O maior valor da lista é {v} e sua na posição {p}',end='')
     contmaior += 1
 elif v == max(lista) and contmaior > 0:
     print(f'... {p}')
print('')


#MOSTRANDO MENOR VALOR
for p,v in enumerate(lista):
 if v==min(lista) and contmenor == 0:
     print(f'O menor valor da lista é {v} e sua posção é {p} ',end='')
     contmenor += 1
 elif v == min(lista) and contmenor > 0:
     print(f'...{p}')

print('')
