'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números que
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
#NÃO ENTENDI MUITO BEM
acumulador = 0
contador = 0
for n in range(1,501,2):
    if (n % 3== 0):
        acumulador = acumulador+ n
        contador = contador +1

print(' A soma de todos os {} valores solicitados é {}'.format(contador,acumulador))




