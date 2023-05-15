'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
distancia = float(input('QUAL A DISTÂNCIA DA VIAGEM (KM): '))
formula200 = 0.50 * distancia
formulalonga = 0.45 * distancia
if(distancia > 200):
    print('Você vai pagar {}R$ '.format(formulalonga))
else:
    print('Você vai pagar {}R$ '.format(formula200))

