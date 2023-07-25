'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input("Digite um número inteiro:" ))
print('''[1]- para binário
[2]- para octal
[3]- para hexadicmal''')
usubase =str(input("qual será a base de conversão: "))
if(usubase == '1'):
    print("O número {} convertido para binário vai ficar {}" . format(num, bin(num)[2:]))
elif(usubase == '2'):
    print("O número {} convertido para octal vai ficar {} ".format(num,oct(num)[2:]))
elif(usubase == '3'):
    print("O número {} convertido para a base hexadecimal vai ficar {} ".format(num, hex(num)[2:]))
else:
    print("opção inválida. Tente novamente")
    while(usubase!= '1' or usubase!= '2' or usubase!= '3'):
        usubase = str(input("qual será a base de conversão: "))
        if (usubase == '1'):
            print("O número {} convertido para binário vai ficar {}".format(num, bin(num)[2:]))
        elif (usubase == '2'):
            print("O número {} convertido para octal vai ficar {} ".format(num, oct(num)[2:]))
        elif (usubase == '3'):
            print("O número {} convertido para a base hexadecimal vai ficar {} ".format(num, hex(num)[2:]))
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE")
        if(usubase == '1' or usubase=='2' or usubase=='3'):

            break
print("Programa encerrado")






