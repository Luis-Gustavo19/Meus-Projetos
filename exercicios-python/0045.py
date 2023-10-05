'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
from time  import sleep
#MOSTRAR OPÇÕES
print("\033[0;35mVAMOS JOGAR JOKENPO")
print('[1]- pedra')
print("[2]- papel")
print('[3]- tesoura \033[m')
#PERGUNTAR QUAL OPÇAO DO USUARIO
usu =int(input('Ecolha usa opção: '.strip()))
print('JO')
sleep(1)
print("KEN")
sleep(1)
print('PO')
print('=-='*20)
if(usu==1):
    print("Você jogou pedra")
elif(usu==2):
    print("Você jogou papel")
elif(usu==3):
    print("Você jogou tesoura")
else:
    while(usu != 1,2,3):
        usu = int(input('Ecolha usa opção: '.strip()))
        if (usu == 1):
            print("Você jogou pedra")
        elif (usu == 2):
            print("Você jogou papel")
        elif (usu == 3):
            print("Você jogou tesoura")
            if(usu==1,2,3):
                break
comp = random.randint(1,3)
if(comp==1):
    print("Computador jogou pedra")
elif(comp==2):
    print("computador jogou papel")
elif(comp==3):
    print("Computador jogou tesoura")
print('=-=' *20)
if(usu==comp):
    print('JOGO EMPATADO')
elif(usu ==1 and comp == 2  ):
    print('O computador ganhou')
elif(usu ==2 and comp == 1):
    print('Você ganhou!')
elif(usu ==3 and comp ==1):
    print('O computador ganhou.')
elif(usu ==1 and comp == 3):
    print('Você ganhou.')
elif(usu == 2 and comp ==3):
    print('O computador ganhou.')
elif(comp ==2 and usu==3):
    print('Você ganhou!')