'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

'''n = int(input('Digite um número para ver sua tabuada: '))
cont = 0
while True:
    multi = n * cont
    print(f'{n} X {cont} = {multi} ')
    cont = cont + 1
    if(cont > 10):
        n = int(input('Qual seu próximo valor: '.strip()))
        cont = cont - 10
    if(n <0):
        print('PROGRAMA ENCERRADO...')
        break
'''
#
print("Bem-vindo ao elevador!")
andar_atual = int(input("Em que andar você está? "))
print("Você está no andar", andar_atual)

andar_destino = int(input("Para qual andar você deseja ir? "))
if andar_destino > andar_atual:
    print("O elevador está subindo...")
    for i in range(andar_atual, andar_destino + 1):
        print("Andar", i)
    print("Chegamos ao andar", andar_destino)
elif andar_destino < andar_atual:
    print("O elevador está descendo...")
    for i in range(andar_atual, andar_destino - 1, -1):
        print("Andar", i)
    print("Chegamos ao andar", andar_destino)
else:
    print("Você já está nesse andar!")

