'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Qual o seu nome completo :')).lower().strip()
nomediv = nome.split()
print('Seu primeiro nome é: {}'.format(nomediv[0]))
print('Seu último nome é: {}'.format(nomediv[len(nomediv)-1]))