'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
idadehomemmaisvelho = 0
nomehomemvelho = 0
mulheresmenosde20 = 0
media = 0
for c in range(1,5):
    print('\033[0;36m=-=-=-=-=-=-=-{} Pessoa.=-=-=-=-=-=-=-\033[m'.format(c))
    peg1 = str(input('Nome: '.strip().lower()))
    peg2 = int(input('Idade: '.strip()))
    peg3 = str(input('Sexo - (m/f): '.lower().strip()))
    media =media + peg2
    if (c == 1 and peg3 == 'm'):
        nomehomemvelho = peg1
        idadehomemmaisvelho = peg2
    if(peg3 == 'm' and peg2 > idadehomemmaisvelho):
        idadehomemmaisvelho =peg2
        nomehomemvelho = peg1
    if(peg3 == 'f' and peg2 < 20):
        mulheresmenosde20 = mulheresmenosde20 + 1
print('\033[0;36mNo total, temos {} mulher(es) menores de 20 anos.'.format(mulheresmenosde20))
print('A média de idade de todos é {}'.format(media / 4))
print('A idade do homem mais velho é: {} e seu nome é: {}\033[m'.format(idadehomemmaisvelho,nomehomemvelho))
