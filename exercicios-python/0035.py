'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo'''
reta1 = float(input("Digite o segmento da reta: "))
reta2 = float(input("Digite o segmeneto da segunda reta: "))
reta3 = float(input("Digite o segmento da terceira reta: "))
# A soma de dois lados deverá ser maior que a do terceiro lado.
if(reta3 + reta2 >reta1 and reta3 + reta1 > reta2 and reta2 + reta1 > reta3):
    print("Com essas medidas é possível formar um triângulo.")
else:
    print("Não é possível formar um triângulo com esses segmentos.")