'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''
nomecomp = str(input('Digite seu nome completo: '))
nomecompmai = nomecomp.upper()
print('Seu nome em maiúsculo é:{}'.format(nomecompmai))
nomecompmin = nomecomp.lower()
print('Seu nome muinúsculo é:{}'.format(nomecompmin))
#nome maiusculo e minusculo feito
nomesemesp = nomecomp.replace(' ','')
letrasaotodo = len(nomesemesp)
print('seu nome tem um total de {} letras'.format(letrasaotodo))
#quantas letras tem ao todo certo
letrasprimeironome =nomecomp.split()
primeironome = letrasprimeironome[0]
letrasprimeironome2 =len(primeironome)
print('seu primeiro nome tem {} letras'.format(letrasprimeironome2))