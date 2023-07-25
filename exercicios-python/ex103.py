'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='',gols=0):
    if nome.strip() =='':
        nome ='<desconhecido>'

    if gols == str:
        gols=0
    if isinstance(gols, str) == True:
        gols=0

    a =f'O jogador {nome} fez {gols} gols no campeonato'
    return a


print(ficha('Gustavo',4))





