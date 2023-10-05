'''Exercício Python 62: Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
'''p1 = int(input('Digite o primeiro termo da sua PA: '))
raz = int(input('Digite a razão da sua PA: '))
nter = int(input('Digite o número de termos que deseja para PA: '))
cont = 1
print(p1,'--⊳',end='')
while cont <nter:
    p1 = p1 + raz
    cont = cont + 1
    print(p1,'--⊳',end='')
print('fim')'''
p1 = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digte a razão da PA: '))
cont = 0
cont2 = 0
cont3 = 10
vcps = False
print(p1,'--⊳',end='')
while cont < 9:
    p1 = p1 + raz
    cont = cont + 1
    print(p1,'--⊳',end='')
print('PAUSA')
while not vcps:
    term = int(input('Quantos termos a mais você deseja adicionar: '))
    cont3 = cont3 + term
    if(term == 0):
        vcps = True
    else:
       cont2 = cont2 - cont2
    while cont2 < term :
        p1 = p1 + raz
        cont2  = cont2 + 1
        print(p1,'--⊳',end='')

print('Fim')
print('Você utilizou {} termos no total'.format(cont3))
