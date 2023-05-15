'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
geral =[]
import statistics
dadospessoas= {}
vcps = False
while vcps == False:
    dadospessoas['Nome']=str(input('Digite seu nome: '.strip()))
    dadospessoas['sexo[M/F]'] = str(input('Digte o seu sexo: ')).strip().upper()[0]
    while dadospessoas['sexo[M/F]'] !='M' and dadospessoas['sexo[M/F]'] != 'F':
        print('Digite apenas \033[1;34m"M"\033[m ou \033[1;34m"F"\033[m')
        dadospessoas['sexo[M/F]'] = str(input('Digte o seu sexo: ')).strip().upper()[0]
    dadospessoas['idade'] = int(input('Digite sua idade: '.strip()))
    geral.append(dadospessoas.copy())
    dadospessoas.clear()
    op = str(input('Deseja continuar-[S/N]: ')).strip().upper()[0]
    while op != 'S' and op!='N':
        print('\033[1;31mERRO\033[m Digite apenas com \033[1;34m "S"\033[m ou \033[1;34m"N"\033[m')
        op = str(input('Deseja continuar-[S/N]: ')).strip().upper()[0]
    if op =='N':
        break
qpessoas = 0
mediaidade =[]
mulheres=[]
print('\033[1;34m-=\033[m' * 50)
for k,v in enumerate(geral):
    #print(geral[k]['Nome'])
    if geral[k]['Nome'] not in '':
        qpessoas +=1
print(f'   O total de pessoas cadastradas é {qpessoas}')
print('\033[1;34m-=\033[m' * 50)
for k,v in enumerate(geral):
    if geral[k]['idade']:
        mediaidade.append(geral[k]['idade'])
print(f'   A média de idade de todas as pessoas é {statistics.mean(mediaidade):.2f}')
print('\033[1;34m-=\033[m' * 50)
for k,v in enumerate(geral):
    if geral[k]['sexo[M/F]'] == 'F':
        mulheres.append(geral[k]['Nome'])
if len(mulheres) >=1:
    print(' De mulheres Cadastradas, Temos:\n ')
    for z in mulheres:
        print(z,end=' ''.')
print(' ')
print('\033[1;34m-=\033[m' * 50)
pamedia =[]
print(f'Das pessoas com Idade acima da média temos'
      f':')
for k,v in enumerate(geral):
    if geral[k]['idade'] > statistics.mean(mediaidade):
        pamedia.append(geral[k]['Nome'])
        for c in pamedia:
            print(c)
print('\033[1;34m-=\033[m' * 50)