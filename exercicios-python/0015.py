#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO POR UM CARRO ALUGADO
#E A QUANTIDADE DE DIAS PELO QUAIS ELE FOI ALUGADO.CALCULE O PREÇO A PAGAR, SABENDO QUE
#O CARRO CUSTA 60R$ POR DIA E 0,15 R$ POR KM RODADO
km = float(input('Quantos km percorrido pelo carro:'))
dias = int(input("Quantos dias ele foi alugado:"))
pgdias = 60 * dias
pgrodados = km * 0.15
total = pgdias + pgrodados
print("Você vai pagar um total de {} R$.".format(total))