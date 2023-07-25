'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma
 apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''
soma = 0
cont = 0
for c in range(1,7):
    n = int(input("\033[0;34m Digite o {} número inteiro: ".format(c)))
    if(n % 2 == 0 ):
        soma = soma + n
        cont = cont + 1
print('Você informou {} valores pares e a soma foi {}'.format(cont,soma))