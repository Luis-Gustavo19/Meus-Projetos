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
Qual andar você está:\033[m '''.strip()))

if pergunta >5:
    while pergunta >5:
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
    print('Elevadores Lotados. Aguarde um momento.')
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
    lista = [deci2,deci3]
    menorvalordalista1 = min(lista)
    if menorvalordalista1 == deci2 and menorvalordalista1 == deci3:
        desempate1 = [distancia2,distancia3]
        menorvalordesempate1 = min(desempate1)
        if(menorvalordesempate1 == distancia2):
            print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
        else:
            print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você')
    elif(menorvalordalista1 == deci2):
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    elif(menorvalordalista1 == deci3):
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você.')
        print('\033[1;31m=-=\033[m' * 25)

elif pessoas2 == 5:
    lista3 = [deci1,deci3]
    menorvalordalista2 = min(lista3)
    if menorvalordalista2 == deci1 and menorvalordalista2 == deci3:
        desempate2 = [distancia1,distancia3]
        menorvalordesempate2 = min(desempate2)
        if(menorvalordesempate2 == distancia1):
            print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        else:
            print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você')
    if(menorvalordalista2 == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você. ')
        print('\033[1;31m=-=\033[m'* 25)
    else:
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você. ')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas3 == 5):
    lista4 = [deci1,deci2]
    menorvalordadecisao3 = min(lista4)
    if menorvalordadecisao3 == deci1 and menorvalordadecisao3 == deci2:
        desempate3 = [distancia1,distancia2]
        menorvalordesempate3 = min(desempate3)
        if(menorvalordesempate3 == distancia1):
            print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        else:
            print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você')
    if(menorvalordadecisao3 == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    else:
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas1 ==5 and pessoas2 ==5):
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas3 == 5 and pessoas1 == 5):
    print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
    print('\033[1;31m=-=\033[m'* 25)
elif pessoas3 ==5 and pessoas2 ==5:
    print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
    print('\033[1;31m=-=\033[m' * 25)
else:
    deci1 = distancia1 + pessoas1
    deci2 = distancia2 + pessoas2
    deci3 = distancia3 + pessoas3
    lista = [deci1, deci2, deci3]
    menorvalordalista = min(lista)
    if(menorvalordalista == deci1 and menorvalordalista == deci2 and menorvalordalista == deci3):
        desempate4 = [distancia1 , distancia2,distancia3]
        menorvalordesempate4 = min(desempate4)
        if(menorvalordesempate4 == distancia1):
            print('Visando preservar a estrutura do elevador,o elevador 1 está indo até você')
        elif (menorvalordesempate4 == distancia2):
            print('Visando preservar a estrutura do elevador,o elevador 2 está indo até você')
        elif (menorvalordesempate4 == distancia3):
            print('Visando preservar a estrutura do elevador,o elevador 3 está indo até você')
        elif menorvalordesempate4 == distancia1 and menorvalordesempate4 == distancia2:
            elevas = ['elevador 1', 'elevador 2']
            sort = random.choice(elevas)
            print('Visando preservar a estrutura do elevador, o {} está indo até voce'.format(sort))
        elif menorvalordesempate4 == distancia3 and menorvalordesempate4 == distancia2:
            elevas = ['elevador 2', 'elevador 3']
            sort = random.choice(elevas)
            print('Visando preservar a estrutura do elevador, o {} está indo até você.'.format(sort))
        elif menorvalordesempate4 == distancia1 and menorvalordesempate4 == distancia3:
            elevas = ['elevador 1', 'elevador 3']
            sort = random.choice(elevas)
            print('Visando preservar a estrutura do elevador. o {} está indo até você.')
    if menorvalordalista== deci1:
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você')
    elif menorvalordalista == deci2:
        print(' Visando preservar a estrutura do elevador, o elevador 2 está indo até você')
    elif menorvalordalista == deci3:
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você')