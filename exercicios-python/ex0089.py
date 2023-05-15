'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
alunos_e_notas =[]
listona = []
cont = -1
vcps= False
while vcps == False:
    nome = str(input('Digite o nome do aluno: '.strip().capitalize()))
    alunos_e_notas.append(nome)
    nota1 = float(input('Digite a primeira nota: '))
    alunos_e_notas.append(nota1)
    nota2 = float(input('Digite a segunda nota: '.strip()))
    alunos_e_notas.append(nota2)
    listona.append(alunos_e_notas[:])
    alunos_e_notas.clear()
    per = ' '
    while per != 's' and per!= 'n':
        per = str(input('Deseja continuar-[s/n]'.lower().strip()))
        if per =='s':
            pass
        if per =='n':
            vcps = True
            print('\033[1;31mMÉDIA\033[m')
            print('\033[1;39mNº    NOME    MÉDIA\033[m')
            print('________________________________')
            for c in listona:
                cont +=1
                print(f'{cont}º {c[0]}',end='')
                print(' ',end='')
                print(f' {(c[1] + c[2]) / 2}')
            print('________________________________')
            vcps2= False
            while vcps2 == False:
                if 2 +2 ==4:
                    while vcps2 == False:
                        per2 = int(input('Deseja ver a nota de qual aluno: '.strip()))
                        if per2 > cont or per2 < 0:
                            print('Aluno não existe')
                            vcps2 = True
                        print(f'NOME: {listona[per2][0]}')
                        print(f'NOTA 1: {listona[per2][1]}'), print(f'NOTA 2: {listona[per2][2]}')
                        pf = ''
                        while pf != 's' and pf !='n':
                            pf = str(input('Deseja continuar[S/N]:  ')).lower().strip()
                            if pf == 'n':
                                vcps2 = True
                            if pf =='s':
                                pass
print('PROGRAMA ENCERRADO')