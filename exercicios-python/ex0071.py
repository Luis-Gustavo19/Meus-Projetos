'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
 vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''
print('='*66)
print('{:^66}'.format('BANCO DO GUSTAVO'))
print('='*66)
ced50 = 50
ced20 = 20
ced10 = 10
ced1 =1
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
dinheiro = int(input('Digite o valor a ser sacado R$: '.strip()))
caixa = 0
while dinheiro > caixa:
        caixa += ced50
        cont50 +=1
while caixa > dinheiro:
        caixa -= ced50
        cont50 -=1
while caixa < dinheiro:
        caixa += ced20
        cont20 += 1
while caixa > dinheiro:
        caixa -= ced20
        cont20 -= 1
while caixa < dinheiro:
        caixa += ced10
        cont10 += 1
while caixa > dinheiro:
        caixa -= ced10
        cont10 -=1
while caixa < dinheiro:
        caixa += ced1
        cont1 += 1
while caixa > dinheiro:
        caixa -= ced1
        cont1 -= 1
while caixa == dinheiro:
        break
print(f'O valor solicitado para saque foi: {dinheiro}')
if cont50 >= 1:
    print(f'{cont50} Cédulas de R$50.00 ')
if cont20 >=1:
    print(f'{cont20} Cédulas de R$20.00')
if cont10 >= 1:
    print(f'{cont10} Cédulas de R$10.00')
if cont1 >= 1:
    print(f'{cont1} Cédulas de R$1.00 ')