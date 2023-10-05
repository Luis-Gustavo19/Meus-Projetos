'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
ncomp = random.randint(1,10)
print(ncomp)
njoga = int(input('Qual número o computador pensou de 1 a 10: '))
chutes = 1
if(ncomp == njoga):
    print('Parabéns, você acertou com {} tentativa'.format(chutes))
else:
    while ncomp != njoga:
        if(njoga > ncomp):
            print('Menos...')
        else:
            print('Mais...')
        print('Você errou. tente novamente.')
        chutes += 1
        njoga = int(input('Qual número estou pensando de 1 a 2: '))
    print('parabéns, você acertou com {} tentativas.' .format(chutes))
