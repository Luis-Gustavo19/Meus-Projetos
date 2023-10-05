'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
nas = int(input("Em que ano você nasceu? "))
idade = 2022 - nas
print("O atleta tem {} anos.".format(idade))
if(idade <=9) :
    print("Sua categoria é Mirim")
elif(idade >=10 and idade <= 14):
    print(' \033[7;30m Sua categoria é Adolescente.\033[m')

elif(idade >=15 and idade <=19):
    print("\033[1;33m Sua categoria é Junior")

elif(idade <=25):
    print(" \033[1;31m Sua categoria é Sênior")

else:
    print(" \033[1;32m Sua categoria é Master")
