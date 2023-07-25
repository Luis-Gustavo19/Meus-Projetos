'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
print('VAMOS JOGAR PAR OU ÍMPAR')
vida = 1
vitorias = 0
while True:
    if(vida == 0):
        break
    n = int(input('\033[1;33mDigite um valor: \033[m'))
    pouijog = str(input('\033[1;36mQUAL VOCÊ ESCOLHE [P/I]\033[m'.strip().lower()))
    if pouijog == 'p' or pouijog =='i':
        opcaoescolhida =pouijog
        comp = random.randint(1,10)
        soma = n + comp
        print(f'Você digitou o valor {n}. O computador jogou o número {comp}. O total deu {soma}')
        venouperd = soma % 2
        if(opcaoescolhida == 'p' and venouperd ==0):
            vitorias = vitorias + 1
            print('\033[1;32mPARABÉNS!!! VOCÊ GANHOUU!!! \033[m')
            print(f'Você tem {vitorias} vitoria(s)')
        else:
            vida = vida-1
            print('\033[1;30mO computador ganhou. Você perdeu =(\033[m')
            print('\033[1;35mGAME OVER\033[m')
    else:
        print('\033[1;31mDigito inválido.\033[m')








