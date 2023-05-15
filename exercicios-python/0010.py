#ler quanto tem na carteira e postrar o valor em dolar
carteira = float(input("quanto de dinheiro (R$) você tem na carteira: "))
md = (5.25)
covdol =( carteira / md)
print("com {} reais você terá : {:.2f} doláres".format(carteira,covdol))