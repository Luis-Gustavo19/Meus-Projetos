'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
frase = str(input("Digite sua frase: ")).strip()
semesp = frase.replace(' ','')
fraseinvertida =semesp [::-1]
if(fraseinvertida == semesp):
   print(" O inverso de {} fica {}".format(frase,fraseinvertida))
   print("\033[35m Temos um palindromo")


else:
    print('\033[31m NÃO TEMOS UM PALÍNDROMO')






































#lista = [frase]
#print(lista[0:][-1:1])