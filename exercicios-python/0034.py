'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input("Digite seu salário R$: "))
if(salario >= 1250):
    aumeneto =  salario * 10/100
    salario_novo = salario + aumeneto
    print('COM UM AUMENTO DE 10% O SEU SALÁRIO PASSARÁ A SER {:.2f}R$ '.format(salario_novo))
else:
    aumento15 = salario * 15/100
    salario_novo2 = salario + aumento15
    print(" O SEU SALÁRIO AGORA VAI PASSAR A SER {:.2f}R$".format(salario_novo2))