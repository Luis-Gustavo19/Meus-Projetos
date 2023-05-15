'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
reta1 = float(input("Digite o primeiro segmento: "))
reta2 = float(input("Digite o segundo segmento: "))
reta3 = float(input("Digite o terceiro segmento: "))
if(reta1 + reta2 >reta3 and reta2 + reta3 > reta1 and reta3 +reta1 > reta2):
    print("Com esses segmentos é possível formar um triângulo ", end ='')
    if (reta1 == reta2 and reta1 and reta2 == reta3):
        print("Equilátero")
    elif(reta1 == reta2 != reta3 or reta3==reta1 != reta2 or reta2 ==reta3 != reta1):
        print("Isósceles")

    else:
        print("Escaleno")



else:
    print('Não é possível formar um triângulo com essas medidas')
