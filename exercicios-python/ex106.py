'''Exercício Python 106: Faça um mini-sistema que
utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
o programa se encerrará. Importante: use cores.'''
print('Sistema de Ajuda para Bibliotecas Python')
while True:
    ajuda = str(input('\033[7;36mDigite aqui a biblioteca que você tem dúvida: \033[m'))
    print('\033[7;37m')
    help(ajuda)
    print('\033[m')
    if ajuda.lower().strip() == 'fim':
        break
