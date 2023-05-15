#FAÇA UM PROGRAMA QUE LEIA O SALÁRIO DE UM FUNCIONARIO E MOSTRE
# SEU NOVO SALÁRIO COM 15% DE AUMENTO
salario = float(input("Qual seu salário R$: "))
novosalario = salario + (salario * 15/100)
print("PARABÉNS, SEU SALÁRIO COM 15% DE AUMENTO VAI AUMENTAR PARA {}".format(novosalario))