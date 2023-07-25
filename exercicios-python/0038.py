'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''
num = int(input("DIGITE UM NÚMERO: "))
num2 = int(input("DIGITE OUTRO NÚMERO: "))
if(num > num2):
    print('O primerio valor é maior.')
elif(num ==num2):
    print("Não existe valor maior, os dois são iguais")

else:
    print("O segundo valor é maior")