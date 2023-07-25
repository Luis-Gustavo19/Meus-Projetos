'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
cont = 0
menva = 0
pmil = 0
tot = 0
pr1 = ''
while True:
    cont +=1
    pr = str(input('Digite o nome do produto: '.strip().lower()))
    valor = float(input('Digite o valor do produto: '))
    tot += valor
    if valor > 1000:
        pmil += 1
    if cont == 1:
        menva = valor
        pr1 = pr
    else:
        if valor < menva:
            menva = valor
            pr1 = pr


    pergunta = str(input('Deseja continuar cadastrando suas compras [S/N]: '.strip().lower()))[0]
    if pergunta == 'n':
        break
print(f'O TOTAL DE SUAS COMPRAS FICOU NO VALOR DE R${tot}')
print(f'Nas suas compras tem {pmil} produtos que custam mais de R$ 1000.')
print(f'O produto mais barato das sua(s) compra(s) é {pr1} e seu valor é {menva}')
