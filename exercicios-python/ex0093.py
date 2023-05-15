'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
gols =[]
cont =0
jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador: '.strip()))
jogador['partidas'] = int(input(f'Digite quantas partidas o \033[1;31m{jogador["nome"]}\033[m jogou:  '))
while cont < jogador["partidas"]:
    cont +=1
    gols.append(int(input(f'Quantos gols na {cont}º partida : ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'\033[1;33m{k}\033[1;34m tem o valor\033[m \033[1;33m{v} \033[m ')
print('-='*30)
print(f'O {jogador["nome"]} tem {jogador["partidas"]} partidas')
for k,c in enumerate(gols):
    print(f'Na {k+1}º partida, fez {c}gols')










