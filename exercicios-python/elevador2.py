import random
from time import sleep

elevador1 = random.randint(0,5)
elevador2 = random.randint(0,5)
elevador3 = random.randint(0,5)
pessoas1 = random.randint(0,5)
pessoas2 = random.randint(0,5)
pessoas3 = random.randint(0,5)
print('\033[1;36mSISTEMA\033[m')
print('\33[1;36m-=-\033[m' * 25)
print('O elevador 1 está no {}° andar e está com {} pessoas'.format(elevador1, pessoas1))
print('O elevador 2 está no {}° andar e está com {} pessoas'.format(elevador2, pessoas2))
print('O elevador 3 está no {}° andar e está com {} pessoas'.format(elevador3, pessoas3))
print('\33[1;36m-=-\033[m' * 25)
pergunta = int(input('''[0]- TÉRREO
[1]- PRIMEIRO ANDAR
[2]- SEGUNDO ANDAR
[3]- TERCEIRO ANDAR
[4]- QUARTO ANDAR
[5]- QUINTO ANDAR
Qual andar você está: '''.strip()))

if pergunta >5:
    while pergunta >5:
        pergunta = int(input('Andar inválido. Digite novamente:   '.strip()))

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
    print('\033[1;36mSISTEMA\033[m')
    print('\33[1;36m-=-\033[m' * 25)
    print('O elevador 1 está no {}° andar e está com {} pessoas'.format(elevador1, pessoas1))
    print('O elevador 2 está no {}° andar e está com {} pessoas'.format(elevador2, pessoas2))
    print('O elevador 3 está no {}° andar e está com {} pessoas'.format(elevador3, pessoas3))
    print('\33[1;36m-=-\033[m' * 25)
if pessoas1 == 5:
    deci2 = distancia2 + pessoas2
    deci3 = distancia3 + pessoas3
    lista2 = [deci2,deci3]
    menorvalordalista1 = min(lista2)
    if(menorvalordalista1 == deci2):
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    else:
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
elif pessoas2 == 5:
    deci1 = distancia1 + pessoas1
    deci3 = distancia3 + pessoas3
    lista3 = [deci1,deci3]
    menorvalordalista2 = (min(lista3))
    if(menorvalordalista2 == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você. ')
        print('\033[1;31m=-=\033[m'* 25)
    else:
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você. ')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas3 == 5):
    deci1 = distancia1 + pessoas1
    deci2 = distancia2 + pessoas2
    lista4 = [deci1,deci2]
    menorvalordadecisao3 = min(lista4)
    if(menorvalordadecisao3 == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    else:
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas1 == 5 and pessoas2 ==5):
    deci3 = distancia3 + pessoas3
    lista5 = [deci3]
    menorvalordalista4 = min(lista5)
    if(menorvalordalista4 == deci3):
        (print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você.'))
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas2 == 5 and pessoas3 == 5):
    deci1 = distancia1 + pessoas1
    lista6 = [deci1]
    menorvalordalista5 =min(lista6)
    if(menorvalordalista5 == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
elif(pessoas3 == 5 and pessoas1 == 5):
    deci2 = distancia2 + pessoas2
    lista7 =[deci2]
    menorvalordalista6 = min(lista7)
    if(menorvalordalista6 == deci2):
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
else:
    deci1 = distancia1 + pessoas1
    deci2 = distancia2 + pessoas2
    deci3 = distancia3 + pessoas3
    lista = [deci1, deci2, deci3]
    menorvalordadecisao = min(lista)
    if(menorvalordadecisao == deci1):
        print('Visando preservar a estrutura do elevador, o elevador 1 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    elif(menorvalordadecisao == deci2):
        print('Visando preservar a estrutura do elevador, o elevador 2 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)
    elif(menorvalordadecisao == deci3):
        print('Visando preservar a estrutura do elevador, o elevador 3 está indo até você.')
        print('\033[1;31m=-=\033[m'* 25)