'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
velocarro = float(input("Digite a velocidade do carro(km): "))
formula = velocarro - 80
multa = formula * 7


if(velocarro >80):
    print('VOCÊ FOI MULTADO E VAI PAGAR {} R$!'.format(multa))
