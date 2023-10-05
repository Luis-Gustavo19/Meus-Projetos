'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
 o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
print('='*10)
print('CADASTRO')
print('='*10)

a = 0
b = 0
c = 0
while True:
    idade = int(input('Digite sua idade: '.strip()))
    if(idade >18):
        a = a + 1
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Digite seu sexo [M/F]: ')).lower().strip()[0]
        if (sexo == 'm'):
            b = b + 1
        if (idade <20 and sexo == 'f'):
            c = c + 1

    pergunta = str(input('Deseja continuar cadastrando?  [S/N]:  '.lower().strip()))[0]
    if pergunta == 'n':
        break
print(f'No total, temos {a} pessoas cadastradas maiores de 18.')
print(f'Temos {b} homens cadastrados.')
print(f'Temos {c} mulheres menores de 20 anos.')