
#Levaremos em consideração apenas 02 parâmetros para efeito de decisão do sistema, são eles:
#- A quantidade de andar que o elevador deverá passar para atender o morador
#- A quantidade de pessoas dentro do elevado
import random
from time import sleep
elevador1 = random.randint(0,5)
elevador2 = random.randint(0,0)
elevador3 = random.randint(0,5)
pessoas1 = random.randint(0,5)
pessoas2 = random.randint(0,5)
pessoas3 = random.randint(0,5)
print('\033[1;36mSISTEMA\033[m')
print('\33[1;36m-=-\033[m' * 25)
print('\33[1;36mO elevador 1 está no {}° andar e está com {} pessoas'.format(elevador1, pessoas1))
print('O elevador 2 está no {}° andar e está com {} pessoas'.format(elevador2, pessoas2))
print('O elevador 3 está no {}° andar e está com {} pessoas\033[m'.format(elevador3, pessoas3))
print('\33[1;36m-=-\033[m' * 25)
pergunta = int(input('''\033[1;33m[0]- TÉRREO
[1]- PRIMEIRO ANDAR
[2]- SEGUNDO ANDAR
[3]- TERCEIRO ANDAR
[4]- QUARTO ANDAR
[5]- QUINTO ANDAR
Qual andar você está:\033[m'''.strip()))
if pergunta >5 or pergunta <0:
    while pergunta >5 or pergunta <0:
        pergunta = int(input('\033[1;31mAndar inválido.\033[m Digite novamente:   '.strip()))
distancia1 = abs(elevador1 - pergunta)
distancia2 = abs(elevador2 - pergunta)
distancia3 = abs(elevador3 - pergunta)
deci1 = distancia1 + pessoas1
deci2 = distancia2 + pessoas2
deci3 = distancia3 + pessoas3
lista = [deci1,deci2,deci3]
while pessoas1 == 5 and pessoas2 == 5 and pessoas3 ==5:
    print('\033[1;36mSISTEMA\033[m')
    print('\033[1;36mElevadores Lotados. Aguarde um momento.\033[m')
    for c in range(1,6):
        print(c)
        sleep(1)
    elevador1 = random.randint(0, 5)
    elevador2 = random.randint(0, 5)
    elevador3 = random.randint(0, 5)
    pessoas1 = random.randint(0, 5)
    pessoas2 = random.randint(0, 5)
    pessoas3 = random.randint(0, 5)
    distancia1 = abs(elevador1 - pergunta)
    distancia2 = abs(elevador2 - pergunta)
    distancia3 = abs(elevador3 - pergunta)
    print('\033[1;36mSISTEMA\033[m')
    print('\33[1;36m-=-\033[m' * 25)
    print('O elevador 1 está no {}° andar e está com {} pessoas'.format(elevador1, pessoas1))
    print('O elevador 2 está no {}° andar e está com {} pessoas'.format(elevador2, pessoas2))
    print('O elevador 3 está no {}° andar e está com {} pessoas'.format(elevador3, pessoas3))
    print('\33[1;36m-=-\033[m' * 25)
if pessoas1 == 5:
    lista1 = [deci2, deci3]
    menorvalorlista1 = min(lista1)
    if (pessoas1 == 5 and pessoas2 == 5):
        print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m ')
    elif (pessoas1 == 5 and pessoas3 == 5):
        print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m ')
    elif(menorvalorlista1 == deci2):
        print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')
    elif(menorvalorlista1 == deci3):
        print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')

    elif(menorvalorlista1 == deci2 and menorvalorlista1 == deci3):
        desempate1 = [distancia2,distancia3]
        menordistancia1 = min(desempate1)
        if(menordistancia1 == distancia2):
            print('\033[1;32mAguarde, o elevador 2 está indo até você. \033[m')
        elif(menordistancia1 == distancia3):
            print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')
        elif(menordistancia1 == distancia2 and menordistancia1 == distancia3):
            com1 = '\033[1;32mAguarde, o elevador 2 está indo até você\033[m'
            com2 = '\033[1;32mAguarde, o elevador 3 está indo até você\033[m'
            sort = [com1,com2]
            print(random.choice(sort))
elif pessoas2 == 5:
    lista2 = [deci1, deci3]
    menorvalorlista2 = min(lista2)
    if (pessoas2 == 5 and pessoas1 == 5):
        print('\033[1;32mAguarde, o elevador 3 está vindo até você. \033[m')
    elif (pessoas2 == 5 and pessoas3 == 5):
        print('\033[1;32mAguarde, o elevador 1 está indo até você. \033[m')
    elif(menorvalorlista2 == deci1):
        print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
    elif(menorvalorlista2 == deci3):
        print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')
    elif(menorvalorlista2== deci1 and menorvalorlista2 == deci3):
        desempate2 = [distancia1,distancia3]
        menordistancia2 = min(desempate2)
        if(menordistancia2 == distancia1):
            print('\033[1;32mAguarde, o elevador 1 está indo até você. \033[m')
        elif(menordistancia2 == distancia3):
            print('\033[1;32mAguarde, o elevador 3 está vindo até você.\033[m')
        elif(menordistancia2 == distancia1 and menordistancia2 == distancia3):
            com3 = '\033[1;32mAguarde, o elevador 1 está indo até você\033[m'
            com4 = '\033[1;32mAguarde, o elevador 3 está indo até você\033[m'
            sort1 = [com3,com4]
            print(random.choice(sort1))
elif pessoas3 == 5:
    lista3 = [deci2, deci1]
    menorvalorlista3 = min(lista3)
    if (pessoas3 == 5 and pessoas1 == 5):
        print('\033[1;32mAguarde, o elevador 2 está indo até você. \033[m')
    elif (pessoas3 == 5 and pessoas2 == 5):
        print('\033[1;32mAguarde, o elevador 1 está indo até você. \033[m')
    elif(menorvalorlista3 == deci1):
        print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
    elif(menorvalorlista3 == deci2):
        print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')

    elif(menorvalorlista3== deci1 and menorvalorlista3 == deci2):
        desempate3 = [distancia1,distancia2]
        menordistancia3 = min(desempate3)
        if(menordistancia3 == distancia1):
            print('\033[1;32mAguarde, o elevador 1 está indo até você. \033[m')
        elif(menordistancia3 == distancia2):
            print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')
        elif(menordistancia3 == distancia1 and menordistancia3 == distancia2):
            com5 = '\033[1;32mAguarde, o elevador 1 está indo até você\033[m'
            com6 = '\033[1;32mAguarde, o elevador 2 está indo até você\033[m'
            sort2 = [com5,com6]
            print(random.choice(sort2))
else:
    lista = [ deci1,deci2,deci3]
    menorvalorlista = min(lista)
    if(menorvalorlista == deci1):
        print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
    elif(menorvalorlista == deci2):
        print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')
    elif(menorvalorlista == deci3 ):
        print('\033[1;32mAguarde, o elevador 3 está indo até você. \033[m')
    elif(menorvalorlista == deci1 and menorvalorlista == deci2 and menorvalorlista == deci3):
        distanciaparadesempate = [ distancia1,distancia2,distancia3]
        menordistancia = min(distanciaparadesempate)
        if(menordistancia == distancia1):
            print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
        elif(menordistancia == distancia2):
            print('\033[1;32mAguarde, o elevador 2 esta indo até você.\033[m')
        elif(menordistancia == distancia3):
            print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')
    elif(menorvalorlista == deci1 and menorvalorlista == deci3):
        desempate4 = [distancia1,distancia3]
        menordistancia4 = min(desempate4)
        if(menordistancia4 == distancia1):
            print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
        elif(menordistancia4 == distancia3):
            print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')
        elif(menordistancia4 == distancia1 and menordistancia4 == distancia3):
            com7 = '\033[1;32mAguarde, o elevador 1 está indo até você.\033[m'
            com8 = '\033[1;32mAguarde, o elevador 3 está indo até você.\033[m'
            sort3 = [com7,com8]
            print(random.choice(sort3))
    elif(menorvalorlista == deci2 and menorvalorlista == deci1):
        desempate5 = [distancia1,distancia2]
        menordistancia5 = min(desempate5)
        if(menordistancia5 == distancia1):
            print('\033[1;32mAguarde, o elevador 1 está indo até você.\033[m')
        elif(menordistancia5 == distancia2):
            print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')
        elif(menordistancia5 == distancia1 and menordistancia5 == distancia2):
            com9 = '\033[1;32mAguarde, o elevador 1 está indo até você.\033[m'
            com10 ='\033[1;32mAguarde, o elevador 2 está indo até você.\033[m'
            sort4 = [com9,com10]
            print(random.choice(sort4))
    elif(menorvalorlista == deci2 and menorvalorlista == deci3):
        desempate6 = [distancia2,distancia3]
        menordistancia6 =min(desempate6)
        if(menordistancia6 == distancia2):
            print('\033[1;32mAguarde, o elevador 2 está indo até você.\033[m')
        elif(menordistancia6 == distancia3):
            print('\033[1;32mAguarde, o elevador 3 está indo até você.\033[m')
        elif(menordistancia6 == distancia2 and menordistancia6 == distancia3):
            com11 = '\033[1;32mAguarde, o elevador 2 está indo até você\033[m'
            com12 ='\033[1;32mAguarde, o elevador 3 está indo até você.\033[m'
            sort5 = [com11,com12]
            print(random.choice(sort5))
