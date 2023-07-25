'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente'''
temporario =[]
tudo =[]
for c in range(0,7):
    temporario.append(int(input(f'Digite o {c +1 }°valor para adicionar a lista: ')))
    #fazendo uma copisa para tudo
    tudo.append(temporario[:])
    temporario.clear()
print('Valores adicionados')
pares =[]
impares =[]
for c in tudo:
    if c[0] %2 ==0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Dos valores adicionados, estes são valores pares = {sorted(pares)}')
print(f'Estes são os valores ímpares: {sorted(impares)}')


tudo = []
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor para adicionar a lista: '))
    tudo.append(valor)

print('Valores adicionados')
pares = []
impares = []
for c in tudo:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Dos valores adicionados, estes são valores pares = {sorted(pares)}')
print(f'Estes são os valores ímpares: {sorted(impares)}')
