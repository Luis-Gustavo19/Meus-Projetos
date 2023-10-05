produto = float(input("qual o preço do produto R$: "))
porcentagem = produto * (5/100)
desconto = produto - porcentagem
print("o produto aplicado o desconto de 5% vai ficar: {}R$".format(desconto))