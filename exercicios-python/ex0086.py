'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''

matriz=[]
num =[]
a =1
digitos =0
cont =1
#ADICIONANDO OS NUMEROS NA LISTA MATRIZ E DIZENDO SUA POSIÇÃO
for c in range(1,10):
    num.append(int(input(f'Digite um valor para a posição[{a},{cont}]: ')))
    digitos +=1
    cont +=1
    if digitos ==3:
        a =2
        cont=1
    if digitos ==6:
        a=3
        cont =1

    matriz.append(num[:])
    num.clear()

#Mostre matriz na tela com formatação correta(uma bosta)
print(f'{matriz[0]}  {matriz[1]}  {matriz[2]}')
print(f'{matriz[3]}  {matriz[4]}  {matriz[5]}')
print(f'{matriz[6]}  {matriz[7]}  {matriz[8]}')
'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna.
 C) O maior valor da segunda linha.'''
#soma valores pares digitados
soma =0
for p in matriz:
    if p[0] %2 ==0:
        soma +=p[0]
print(f'O total da soma de todos os valores pares são {soma}')
#A soma dos valores da terceira coluna
tersoma =matriz[2][0]
tersoma2 =matriz[5][0]
tersoma3 =matriz[8][0]
sominha = tersoma + tersoma2 + tersoma3
print(f'A soama dos elementos da terceira coluna é {sominha}')
#Maior valor da terceira linha
maiorvalor= []
q =matriz[3][0]
maiorvalor.append(q)
w =matriz[4][0]
maiorvalor.append(w)
e =matriz[5][0]
maiorvalor.append(e)
print(f'O maior valor da segunda linha é {max(maiorvalor)}')




