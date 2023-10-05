'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
cont = 0
while True:
    usu = int(input('Adicione um valor a lista: '))
    if usu not in lista:
        lista.append(usu)
        print('Adicionado.')
        print(lista)
    else:
        print('Não adicionei, pois o valor já existe.')
        print(lista)
    opcao = str(input('Deseja continuar adicionando valores-[S/N]: ')).strip().lower()
    while opcao[0] !='s' and opcao[0] !='n':
        opcao = str(input('Dígito inválido. Deseja continuar adicionando valores-[S/N]: ')).strip().lower()
    if opcao[0] =='s':
        pass
    elif opcao[0] =='n':
        break
print(sorted(lista))
