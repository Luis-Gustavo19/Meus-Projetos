'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
#meio bugado kkk melhor refazer
print("=======LOJAS GUSTAVO========")
compras = float(input(('Qual o valor das compras R$: ')))
print('''[1]- À vista dinheiro/cheque.
[2]- À vista no cartão.
[3]- Em até 2x no cartão.
[4]- 3x ou mais no cartão.''')
pergunta = str(input('Digite a opção de pagamento escolhida: ')).strip()
if(pergunta == '1'):
    desconto1 = compras * (10/100)
    comprascomdesc = compras - desconto1
    print("O valor a ser pago será R${:.2f}".format(comprascomdesc))
elif(pergunta == '2'):
    desconto2 = compras * (5/100)
    comprascomdesc2 = compras - desconto2
    print("O valor a ser pago será R${:.2f} ".format(comprascomdesc2))
elif(pergunta =='3'):
    desconto3 = compras / 2
    print("O Valor a ser pago será R${:.2f}.".format(desconto3))
elif(pergunta == '4'):
    dividir = int(input("Em quantas vezes você quer dividir: ".strip()))
    juros = compras * (20/100)
    comprasvalorfinal = (compras + juros) / dividir
    if (dividir > 10):
        while(dividir >10):
            print("O VALOR REQUERIDO É INVÁLIDO.")
            dividir = int(input("Em quantas vezes você quer dividir: ".strip()))


    print("O valor pago será {} pago em parcelas de R${:.2f}" .format(compras,comprasvalorfinal))
else:
    print("forma de pagamento inválido. PROGRAMA ENCERRADO.")

