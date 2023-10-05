"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
def fatorial(num,show=False):
    """

    :param num: numero que você quer quer saber o valor do fatorial
    :param show: (opcional) ver toda a multiplicação do fatorial até seu último elemento
    :return: retorna os valores
    """
    fato =0
    for c in range(num):
        if c ==0:
            continue
        if c ==1:
            fato =num * c
        else:
            fato = fato *c
    if show==False:
        return fato

    if show==True:
        lista =[]
        while num !=0:
            a =str(f'{num} x')
            if num == 1:
                a=str(f'{num}')

            lista.append(a)

            num-=1

            if num ==0:
                b = f'={fato}'
                lista.append(b)
                resultado = ' '.join(lista)
                return resultado


print(fatorial(4,True))
print(help(fatorial))