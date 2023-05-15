'''Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
ano = int(input("Digite o ano: "))
formula = ano % 4
if(formula == 0 ):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")