'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
#lendo quatro valores e colocando na tupla
cont = 0
while cont < 4:
    cont +=1
    n = int(input('Digite um valor: '))
    if cont == 1:
        a = n
    elif cont == 2:
        b = n
    elif cont == 3:
        c = n
    elif cont == 4:
        d = n
tupla = (a,b,c,d)
print('-=-' * 20)
print('O valor 9 aparece ', end='')
print(tupla.count(9), end='')
print(' vez(es) na tupla')
print('-=-' * 20)
if 3 in tupla:
    print(f'O primeiro valor 3 está na posição: {tupla.index(3) +1}')
print('-=-' * 20)
for c in tupla:
    if c % 2 == 0:
        print(f'O valor par é: {c}')
print('-=-' * 20)