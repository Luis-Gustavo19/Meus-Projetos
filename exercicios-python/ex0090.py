'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
cont =0
dicio= {}
while cont <5:
    cont+=1
    dicio['nome'] = str(input('Digite o nome do aluno: ')).capitalize().strip()
    dicio['media'] = float(input(f'Digite a média do {dicio["nome"]}: '.strip()))
if dicio['media'] >=7:
    dicio['situacao'] ='APROVADO'

else:
    dicio['situacao'] ='\033[1;31mREPROVADO\033[m'

for k,v in dicio.items():
    if k =='nome':
        print(f'O nome é {v}')
    elif k =='media':
        print(f'A média é {v}')
    elif k =='situacao':
        print(f'Sua situação é {v}')
#OU
for c,v in dicio.items():
    print(f'{c} é igual a {v}')



print(dicio)