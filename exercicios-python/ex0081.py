'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista =[]
usu = int(input('Digite um valor: '))
lista.append(usu)
false = False
while false ==False:
    op = str(input('Quer continuar [S/N]: ')).upper()[0]
    if op == 'S':
        usu = int(input('Digite um valor: '.strip()))
        lista.append(usu)


    if op != 'S' and op != 'N':
        while op != 'S' and op != 'N':
            op = str(input('Valor inválido Digite[S/N]: ')).strip().upper()
            if op =='S':
                usu = int(input('Digite um valor: '.strip()))
                lista.append(usu)


    if op =='N':
        false = True
        break

if 5 not in lista:
    print('O valor 5 NÃO está na lista')
else:
    print('O valor 5 está na lista')
print(f'Ao total foram digitados {len(lista)} números')
print(sorted(lista,reverse= True))
