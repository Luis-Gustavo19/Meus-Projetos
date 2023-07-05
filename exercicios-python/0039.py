'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
print('''[1]- para masculino 
[2]- para feminino''''')
sexo = str(input("Qual seu sexo: ")).strip()
if(sexo == '1'):
    atual = date.today().year
    nasc = int(input("Em que ano você nasceu?"))
    idade = atual - nasc
    print("Quem nasceu em {} tem {} anos em {} ".format(nasc, idade, atual))
    if (idade == 18):
        print("Você tem que se alistar IMEDIATAMENTE!")

    elif (idade < 18):
        saldo = 18 - idade
        print("Você ainda não tem 18 anos, ainda falta {} anos para o alistameneto. ".format(saldo))
        anodealist = atual + saldo
        print("Você deverá se alistar em  {} ".format(anodealist))

    elif (idade > 18):
        saldo2 = idade - 18
        print("Você já deveria ter se alistado há {} anos".format(saldo2))
        anodealist2 = atual - saldo2
        print("Você deveria ter se alistado em {}".format(anodealist2))
else:
    print("VOCÊ NÃO PRECISA SE ALISTAR")





