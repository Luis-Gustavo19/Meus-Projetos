'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
operacao = []


num = str(input('Digite sua operação matemátcia: ')).strip()
operacao.append(num)

cont1 =num.count('(')
cont2 =num.count(')')
print(cont1)
print(cont2)
if cont1 == cont2:
    print('A expressão é válida')
else:
    print('A expressão é INVÁLIDA')


expr = str(input('Digite a expressão: '))
pilha =[]
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) >0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('Sua expressão está válida')
else:
    print('sua expressão está inválida')




