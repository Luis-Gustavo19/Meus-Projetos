'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''
cid = str(input('digite o nome da cidade: ')).upper().strip()
b = 'SANTO' in cid[0:5]
print(b)