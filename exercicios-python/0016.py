#crie um programa que leia um número real qualquer pelo teclado e mostre na tela
#a sua porção inteira
import math
num = float(input("Digite um número qualquer:"))
arredonum = math.trunc(num)
print(arredonum)