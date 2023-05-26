'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
from time import sleep
'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
estatis = []
while True:
    cont =0
    gols =[]
    jogador ={}
    if len(estatis) ==0:
        jogador['cod'] = 0
    if len(estatis) > 0:
        jogador['cod'] = estatis[len(estatis)-1]['cod'] +1
    jogador['nome'] = str(input('Digite o nome do jogador: '.strip()))
    jogador['partidas'] =int(input(f'Quantas partidas o {jogador["nome"]} jogou: '.strip()))
    cont =0
    while cont< jogador['partidas']:
        cont +=1
        gols.append(int(input(f'Quantos gols ele fez na {cont}º partida')))
    jogador['gols'] =gols[:]
    gols.clear()
    estatis.append(jogador.copy())
    op =str(input('Deseja continuar cadastrando-[S/N]: ')).upper().strip()[0]
    if op == 'N':
        jogador.clear()
        break
    if op =='S':
        pass
    if op != 'S' and op!='N':
        print('OPÇÃO INVÁLIDA')
        print('FECHRANDO...')
        sleep(2)
#Beleza, o programa roda os dados dos jogadores em um dicionário e guarda ele em uma lista(estatis)
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
print('{:<5s}{:<20s}{:<10s}{:<100s}'.format("COD", "NOME", "GOLS", "TOTAL"))
print('_______________________________________________________________')

len_de_veri = 0
while len(estatis) > len_de_veri:
    cod = str(estatis[len_de_veri]["cod"])
    nome = estatis[len_de_veri]["nome"]
    gols = str(estatis[len_de_veri]["gols"])
    total = str(sum(estatis[len_de_veri]["gols"]))

    print('{:<5s}{:<20s}{:<10s}{:100s}'.format(cod, nome, gols, total))
    len_de_veri += 1
op =0
umaitera = 0
cont2 =0
while True:
    verificar_se_encontrou_jogador = 0
    cont2 =0
    op = int(input('Digite o cod para analisar o jogador(999 Encerra o programa): '.strip()))
    if op ==999:
        break
    else:
        n_index_da_lista = len(estatis) -1
        for k,c in enumerate(estatis):
            if estatis[k]['cod']==op:
                for g in c['gols']:
                    cont2 +=1
                    print(f"O jogador {estatis[k]['nome']},na sua {cont2}º partida, fez {g} gols")
                    sleep(0.7)
                    verificar_se_encontrou_jogador =1
            if k == n_index_da_lista and verificar_se_encontrou_jogador == 0:
                print('Erro! Não existe Jogador com este cod')





















