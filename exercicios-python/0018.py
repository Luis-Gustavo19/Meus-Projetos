'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
angulo = float(input("digite o ângulo para saber seu seno,cosseno e tangente:"))
convpradi = math.radians(angulo)
seno = math.sin(convpradi)
cos = math.cos(convpradi)
tang = math.tan(convpradi)
print("O ângulo {}º tem o seno {:.2f} ,cosseno {:.2f} e a tangente {:.2f} ".format(angulo,seno,cos,tang))
