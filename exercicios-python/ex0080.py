'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
#NÃO ENTENDI NADA NADA NADA NADA NADA DE NADA MSM SOU BURRO
lista = []
for c in range(0,5):
    num = int(input('Digite um valor para adicionara a lista: '))
    if c ==0:
        lista.append(num)
    elif num > lista[-1]:
        lista.append(num)
        print('Adicionanado ao final da lista...')
    else:
     pos =0
     while pos < len(lista):
         if num<= lista[pos]:
             lista.insert(pos,num)
             print(f'Adicionando na posição {pos} da lista...')
             break

print(lista)