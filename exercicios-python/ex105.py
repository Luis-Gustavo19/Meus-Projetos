'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

– Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)'''


def notas(*num,sit=False):
    dicio ={}
    quant = len(num)
    maior = max(num)
    menor = min(num)
    media =sum(num) / len(num)
    dicio['Quantidade'] = quant
    dicio['maior-nota'] =maior
    dicio['media'] = media
    dicio['menor-nota'] = menor
    if sit==True:
        if media < 7:
            dicio['situação'] ='RUIM'
        if media >=7:
            dicio['situação'] ='BOA'

    return dicio







print(notas(2,1,10,sit=True))