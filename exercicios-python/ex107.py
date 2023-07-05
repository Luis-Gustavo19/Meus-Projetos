'''Exercício Python 113: Reescreva a função leiaInt()
que fizemos no desafio 104, incluindo agora a possibilidade da
 digitação de um número de tipo inválido. Aproveite e crie também
uma função leiaFloat() com a mesma funcionalidade.'''
a =0
while a ==0:
    try:
        n = int(input('Digite um número inteiro: '.strip()))
        n2 = float(input('Digite um valor real: '.strip()))

    except (ValueError,TypeError):
        print('\033[1;31mErro! Digite corretamente o valor necessário:\033[m')

    except KeyboardInterrupt:
        print('\033[1;31mERRO! O usuário não digiou os dados\033[m')
        n =0
        n2=0
        break
    except Exception as erro:
        print(f'Ocorereu um erro {erro.__cause__}')

    else:
        a =1
        print(n,n2)


