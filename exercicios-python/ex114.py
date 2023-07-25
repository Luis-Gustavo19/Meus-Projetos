'''Exercício Python 114: Crie um código em Python que teste se o site pudim está
acessível pelo computador usado.'''
import requests
try:
    url = 'http://pudim.com.br/'
    print(requests.get(url).status_code)
    if requests.get(url).status_code == 200:
        print('Consegui acessar o site: http://pudim.com.br/   com sucesso')
except:
    print('Ocorreu um erro ao tentar ver o site pudim.com.br')

