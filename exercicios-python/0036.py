'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
#pergunte o valor da casa.
casa_valor = float(input("Digite o valor da casa: "))
#pergunte o salário do comprador
salario_comprador = float(input("Digite o seu salário: "))
#pergunte quantas vezes voc~e vai parcelar
anos =int(input("Em quantos anos você vai pagar?: "))
prestacao_mensal= casa_valor / anos
prestacao_meses =prestacao_mensal /12
trintporcensala = salario_comprador * 30/100
if(prestacao_meses > trintporcensala):
   print('PARA PAGAR UMA CASA DE R${} EM {} ANOS, VOCÊ VAI PAGAR R${:.2f} '.format(casa_valor,anos,prestacao_meses))
   print('EMPRÉSTIMO NEGADO.')
else:
    print("Para pagar uma casa de {} em {} anos, você vai pagar R${:.2f} ".format(casa_valor,anos,prestacao_meses))
    print("valor APROVADO!")

