'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
~~~~~~~~~
'''

def Escrever_mensagem(msg):
    print('~' * len(msg))
    print(f'{msg}')
    print('~' * len(msg))


Escrever_mensagem('Curso de Python no YouTube')
Escrever_mensagem('Curso em Vídeo')
Escrever_mensagem('LG')


