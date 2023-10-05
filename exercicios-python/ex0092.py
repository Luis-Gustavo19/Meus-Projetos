'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import *
anoatual = datetime.today().year
cadastro ={}
cadastro['nome'] = str(input('Digite seu nome: '.strip().upper()))
cadastro['anodenascimento'] = int(input('Digite o ANO de nascimento: '.strip()))
cadastro['idade'] = anoatual - cadastro['anodenascimento']
cadastro['CTTPS'] =int(input('Digite o número da carteira (0 se não tiver): '.strip()))
if cadastro['CTTPS'] != 0:
    cadastro['ano de contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite seu salário: '))
    cadastro['Aposentadoria'] = cadastro['ano de contratação'] + 35 - cadastro['anodenascimento']

for k,v in cadastro.items():
    print(f'{k} é {v}')
print(cadastro)
import tkinter as tk

def on_enter(event):
    print("O cursor do mouse está em cima do botão")

def on_leave(event):
    print("O cursor do mouse saiu do botão")

root = tk.Tk()

button = tk.Button(root, text="Botão")
button.pack()

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()


