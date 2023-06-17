'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def Area(largura,comprimento):
    area = largura * comprimento
    print(f'A área do retângulo com largura {largura} e comrpimento {comprimento} é {area}m²')




#PROGRAMA PRINCIPAL
print('CONTROLE DE TERRENOS')
print('-'*20)
largura = float(input('LARGURA (m) '))
comprimento = float(input('COMPRIMENTO (m): '))
Area(largura,comprimento)