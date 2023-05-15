'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
#TUPLA COM NOME DE PRODUTO ESEU PREÇO
preco = ('computador', 2800.50,'Teclado',60.00,'Monitor',160.00, 'Play Station 3',1200.00,'Mouse',55.00)
cont1 = -1
#tô com dificuldades p fzr esse, porém conseguir
print('=' * 50)
print('LISTAGEM DE PREÇO')
print('=' * 50)
for c in preco:
    cont1 +=1
    if cont1 % 2==0:
        a =(len(c))
        print(c,end='')
        print('.' * (40- a),end='')
    else:
        print(f'R$ {c}')

print('=' * 50)