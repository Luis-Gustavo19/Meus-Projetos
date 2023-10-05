'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
pergunta = str(input('Digite o seu sexo [m/f]:')).lower().strip()
while pergunta != 'm' and pergunta != 'f':
    print('Digito inválido')
    pergunta = str(input('Digite o seu sexo [m/f]:')).lower().strip()
print('SEXO {} REGISTRADO COM SUCESSO'.format(pergunta))
