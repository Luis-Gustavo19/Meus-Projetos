'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.  B) Uma listagem com as pessoas mais pesadas.    C) Uma listagem com as pessoas mais leves.
'''
#demorei mt,mas fiz
vcps = False
nome_e_peso = []
galera = []
c_pesso =0


while vcps == False:
    nome_e_peso.append(str(input('NOME:  '.capitalize())))
    nome_e_peso.append(float(input('Peso: '.strip())))
    c_pesso +=1
    #fazendo uma cópia para tudo
    galera.append(nome_e_peso[:])
    nome_e_peso.clear()
    usu =''
    while usu != 's' and usu != 'n':
        usu = str(input('Deseja continuar -[S/N]:  '.strip().lower()))[0]
        if usu =='s':
            pass
        if usu =='n':
            vcps = True


#VERIFICAÇÃO DOS DADOS DENTRO DA LISTA ONDE CONTÉM TODAS AS IDADES E PESO
pesos=[]
for p in galera:
    pesos.append(p[1])

maior =max(pesos)
menor =min(pesos)
print('\033[1;31m*************************************************************\033[m')
print('\033[1;32m*************************************************************\033[m')
print('\033[1;33m*************************************************************\033[m')
print('\033[1;34m*************************************************************\033[m')

print(f'Ao total foram cadastrados {c_pesso} pessoas')
for p in galera:
    if p[1] == maior:
        print(f'A pessoa mais pesada pesa: {maior}kg e se chama: {p[0]}')

    if p[1] == menor:
        print(f'A pessoa mais leve pesa: {menor}kg e se chama: {p[0]}')

print('\033[1;31m*************************************************************\033[m')
print('\033[1;32m*************************************************************\033[m')
print('\033[1;33m*************************************************************\033[m')
print('\033[1;34m*************************************************************\033[m')

