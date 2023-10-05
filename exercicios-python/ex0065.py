'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
 todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = int(input('Digite um valor: '))
maior = n
menor = n
media = 0 + n
cont = 1
per1 = str(input('Deseja continuar [s/n]: '.lower().strip()))
if per1 == 's':
    vcps = False
    while not vcps:
        n = int(input('Digite o valor: '))
        cont = cont + 1
        media = media + n
        if(n > maior):
            maior = n
        if(n < menor):
            menor = n
        per2 = str(input('Deseja continuar [s/n]: '.lower().strip()))
        if(per2 == 'n'):
            vcps = True
            print('Você digitou {} números'.format(cont))
            print('A média é {:.2f}. '.format(media/cont))
            print('O MAIOR VALOR É {}. O MENOR VALOR É {} '.format(maior,menor))
else:
    print('Você digitou {} números'.format(cont))
    print('A MÉDIA É {}'.format(media/cont))
    print('O maior valor é: {} e o menor valor é: {}'.format(maior,menor))