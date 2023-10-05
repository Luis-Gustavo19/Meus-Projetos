'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista =[]
impar =[]
par = []
while True:
    usu = int(input('Diigte um valor para add a lista: '))
    if usu % 2 == 0:
        lista.append(usu)
        par.append(usu)
    if usu % 2==1:
        lista.append(usu)
        impar.append(usu)
    op = ''
    while op != 's' and op != 'n':
        op =str(input('Quer continuar? [S/N]:  '.lower().strip()))

    if op =='s':
        pass
    elif op =='n':
        break

print(lista)
print(impar)
print(par)