'''Vamos-Criar um menu de opções'''
import os
import sys
#Fazendo arquivo txt na pasta atual

pasta_atual = os.getcwd()
# lista todos diretorios da minha pasta atual
lista = os.listdir(pasta_atual)
# pega o numero de index da minha lista que contem todos os arquivos do diretorio
index_lista = len(lista) - 1
achei = False
for c, v in enumerate(lista):
    if v == 'nomescadastro.txt':
        achei = True
    if c == index_lista and achei == True:
        print('\033[1;32mArquivo nomescadastro já existe na pasta atual\033[m')
    if c == index_lista and achei == False:
        print(
            '\033[1;31mArquivo nomescadastro não existe na pasta tual Logo, vou criar o arquivo para execução do programa!\033[m')

if achei == False:
    arquivo = open("nomescadastro.txt", "w")
    achei = True
    print('\033[1;32mArquivo txt Criado\033[m')

if achei == True:
    arquivo = open("nomescadastro.txt", "r")
    arquivo.close()
#Menu de Cadastro
def Painel():
    print('-=-' * 20)
    print('{:>40}'.format('\033[1;36mCADASTRO\033[m'))
    print(
        '''\033[1;33m1\033[1;34m -Cadastrar Pessoa\033[m\n\033[1;33m2\033[m \033[1;34m\033[1;34m-Ver Pessoas Cadastradas\033[m\n\033[1;33m3\033[m \033[1;34m-Sair do Programa\033[m''')
    print('-=-' * 20)

#opção usuário
while True:
    try:
        Painel()
        op = int(input('\33[1;35mDigite sua opção:\033[m '.strip()))
        while op<=0 or op>3:
            op = int(input('Digite sua opção: '.strip()))



    except (ValueError,TypeError):
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

    except KeyboardInterrupt:
        print('\033[1;31mERRO! Usuário não informou nenhum dado.\033[m')
        sys.exit()



    else:
        passou =True
        if passou ==True:
            if op == 1:
                arquivo = open("nomescadastro.txt", "a")


                while True:
                    try:
                        nome = str(input('Nome: '.strip()))
                        idade = int(input('Digite sua idade: '.strip()))
                        arquivo.write(f'{nome}')
                        arquivo.write(f';{idade}\n')

                        arquivo.close()


                    except (ValueError, TypeError):
                        print('\033[1;31mERRO! Digite os dados Corretamente\033[m')
                    except KeyboardInterrupt:
                        print('\033[1;31mAtalho Interrompido\033[m')
                        break

                    else:
                        print(f'\033[1;32m{nome} Adicionado(a) com sucesso!\033[m')
                        break
            if op ==2:
                nomes_pessoas = []
                idade_pessoas = []
                print('{:>33}'.format('\033[1;39mPESSOAS CADASTRADAS\033[m'))
                arquivo =open('nomescadastro.txt','r')
                conteudo = arquivo.read()
                modificado =conteudo.replace('\n',';')
                lista_string=modificado.split(';')
                arquivo.close()
                for chave,valor in enumerate(lista_string):
                    if chave % 2 ==0:
                        nomes_pessoas.append(valor)
                    else:
                        idade_pessoas.append(valor)
                nomes_pessoas.pop(-1)
                print('-=-'*50)
                dicio = {}
                dicio['dadosnomes'] =nomes_pessoas[:]
                dicio['dadosidade'] =idade_pessoas[:]
                cont2 =len(idade_pessoas)
                cont = 0
                print('{:<22}{:<22}'.format('Nome','Idade'))
                print('---------------------------------------------------------------------------------')
                while cont <cont2:
                    print('{:>12} {:>12}'.format(dicio['dadosnomes'][cont],dicio['dadosidade'][cont]))
                    cont+=1
                print('-=-'*50)
            if op == 3:
                break
