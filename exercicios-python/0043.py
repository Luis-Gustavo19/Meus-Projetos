'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
 mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''
peso = float(input("Digite seu peso (kg): "))
altu = float(input("Digite sua altura (m): "))
imc=  peso /(altu**2)
print(" \033[7m O seu indíce de imc é {:.1f}\033[m" . format(imc))
if(imc < 18.5):
    print("\033[0;34m Abaixo do peso")
elif(imc >=18.5 and imc <=25):
    print("\033[0;32m Peso ideal")
elif(imc >25 and imc <30):
    print("\033[0;33m Sobrepeso")
elif(imc >30 and imc <40 ):
    print("\033[0;31m Obesidade")
else:
    print('\033[0;31m Obesidade mórbida')