'''Exercício Python 101: Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
e OBRIGATÓRIO nas eleições.
'''

def voto(ano_nascimento):
    from datetime import date
    data_atual = date.today()
    ano = data_atual.year
    if ano -ano_nascimento >=18 and ano -ano_nascimento<=70:
        resul = f"O voto é obrigatóto com sua idade de {ano-ano_nascimento} anos."
        return resul
    elif ano - ano_nascimento <=16:
        resul = f"Voto Negado. Você só tem { ano - ano_nascimento} anos"
        return resul
    else:
        resul = f"O voto é opcional na sua idade de {ano-ano_nascimento} anos"
        return resul

print(voto(2006))
valor = voto(2008)
