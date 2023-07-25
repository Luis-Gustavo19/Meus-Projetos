'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
from time import sleep
vcps = 0
cont = 0
listona=[]
listinha =[]
#Fazer a lista ser gerada sem se repetir os seis valores
per = int(input('Quantos palpites você quer: '.strip()))
while cont < per:
    vcps=0
    cont+=1
    while len(listinha) <6 and vcps <=1:
        ran = random.randint(1,60)
        if len(listinha) ==0:
            listinha.append(ran)
        if len(listinha) >0:
            while ran is listinha:
                ran = random.randint(1,60)
            if ran not in listinha:
                    listinha.append(ran)
        if len(listinha) ==6:
            listona.append(listinha[:])
            vcps = 100000
            listinha.clear()
#fiz a listinha não repetir os seis valores. e colocar a listinha na listona
#Fiz o numero de listas que o usuário pedir p fazer
cont2= 0
for c in listona:
    cont2 +=1
    print(f'Jogo {cont2}',c,'\n'), sleep(1)








