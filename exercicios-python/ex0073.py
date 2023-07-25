'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
 de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense'''
times = ('Flamengo','Palmeiras','Santos','São Paulo','Corinthians','Goias','Fortaleza', 'Bragantino','Chapecoense','Ceara',
         'Gremio','Cruzeiro','AtleticoMg','AthleticoPR','Internacional','Vasco','Fluminense','Botafogo','Bahia','AmericMG')
#OS CINCO PRIMEIROS
print('PRIMEIROS COLOCADOS')
print('-=-' * 20)
cont = 0
for c in times:
    print(c)
    cont +=1
    if cont ==5:
        break
#ÚLTIMOS COLOCADOS
print('-=-' * 20)
print('ÚLTIMOS COLOCADOS')
print('-=-' * 20)
cont2 = 0
for c in times:
    cont2 +=1
    if cont2 == 17 or cont2 == 18 or cont2==19 or cont2==20:
        print(c)
print('-=-' * 20)

print('='*247)
print('TIMES EM ORDEM ALFABÉTICA')
for c in times:
    print(sorted(times))
    break
print('='*247)
#Em que posição está a chapecoense
#dois métodos
cont3 =0
for c in times:
    cont3+=1
    if c =='Chapecoense':
        print(f'{c} na posição {cont3}')
print(f'O chapecoense está na posição {times.index("Chapecoense")+1}')
















