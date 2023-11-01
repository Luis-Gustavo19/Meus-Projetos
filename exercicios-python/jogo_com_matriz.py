import tkinter as tk
from tkinter import messagebox
from random import randint
from time import sleep
#JOGO PARA O USUÁRIO ESCOLHER ALGUM LUGAR ENA MATRIZ E  TENTAR ACERTAR QUAL POSIÇÃO ESTÁ A VITÓRIA, ONDE O
#COMPUTADOR VAI FAZER A MSM COISA, PORÉM AUTOMÁTICAMNETE
matriz = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# Função para lidar com o clique no botão "Jogar"
# Função para criar e exibir a matriz em uma janela
historico_jogadas = []  # Mova a declaração para fora da função

def jogar():
    linha_sort = randint(0, 2)
    coluna_sort = randint(0, 2)

    tupla_sorteada = linha_sort, coluna_sort



    def exibir_matriz():
        for i in range(3):
            for j in range(3):
                # Crie um rótulo para cada elemento da matriz (asterisco)
                elemento = tk.Label(nova_janela, text=matriz[i][j], font=("Arial", 24), width=5, height=2)
                elemento.grid(row=i, column=j)  # Organize os rótulos em uma grade

    def validar_dados_e_fazer_jogada():
        linha = linha_tk.get()
        coluna = coluna_tk.get()


        try:
            # Tente converter a string em um inteiro
            linha_alvo = int(linha) -1
            coluna_alvo = int(coluna) -1

        except ValueError:
            # Se a conversão falhar, exiba uma mensagem de erro
            messagebox.showerror("Erro", "Digite um número válido")
            return  # Retorna para evitar o processamento adicion
            # al

        if linha_alvo < 0 or linha_alvo > 2:
            messagebox.showerror("Erro", f"Digite uma linha entre: 1, 2 e 3")
        elif coluna_alvo < 0 or coluna_alvo > 2:
            messagebox.showerror("Erro", f"Digite uma coluna entre: 1, 2 e 3")
        else:
            tupla_usu = linha_alvo, coluna_alvo
            if tupla_usu in historico_jogadas:
                messagebox.showwarning('ESCOLHA OUTRO LUGAR', 'Este local já foi marcado, tente outro!')
            else:

                if tupla_sorteada == tupla_usu:
                    matriz[linha_alvo][coluna_alvo] = 'WIN'  # Atualize a matriz com 'X'
                    exibir_matriz()  # Atualize a interface gráfica
                    messagebox.showinfo('VITÓRIA', 'Parabéns você ganhou o jogo!')
                    historico_jogadas.append(tupla_usu)

                    sleep(3)
                    quit()

                matriz[linha_alvo][coluna_alvo] = 'X'  # Atualize a matriz com 'X'
                exibir_matriz()  # Atualize a interface gráfica
                historico_jogadas.append(tupla_usu)
                #aqui termina a funk do usuario

                def computador_jogando():
                    pronto_label = tk.Label(nova_janela, text="", font=("Helvetica", 20))
                    pronto_label.grid(row=3,column=25)
                    nova_janela.grab_set()  # Impede a interação com a janela principal
                    pronto_label.config(text="Aguarde...")
                    botao_confirmar.config(state=tk.DISABLED)  # Desabilita o botão durante o carregamento
                    nova_janela.update_idletasks()  # Força a atualização da janela

                    # Simule um carregamento e vai fazer a jogada automatica do computador
                    nova_janela.after(3000)
                    comp_linha = randint(0,2)
                    comp_coluna = randint(0,2)
                    tupla_comp = comp_linha, comp_coluna
                    if tupla_comp in historico_jogadas:
                        while tupla_comp in historico_jogadas:
                            comp_linha = randint(0, 2)
                            comp_coluna = randint(0, 2)
                            tupla_comp = comp_linha, comp_coluna
                        if tupla_sorteada == tupla_comp:
                            matriz[comp_linha][comp_coluna] = 'WIN'  # Atualize a matriz com 'X'
                            exibir_matriz()  # Atualize a interface gráfica
                            historico_jogadas.append(tupla_comp)
                            messagebox.showinfo('DERROTA', 'O computador ganhou o jogo!')
                            sleep(3)
                            quit()
                        else:
                            matriz[comp_linha][comp_coluna] = 'O'  # Atualize a matriz com 'O'
                            exibir_matriz()  # Atualize a interface gráfica
                            historico_jogadas.append(tupla_comp)


                    else:
                        if tupla_sorteada == tupla_comp:
                            matriz[comp_linha][comp_coluna] = 'WIN'  # Atualize a matriz com 'win'
                            exibir_matriz()  # Atualize a interface gráfica
                            historico_jogadas.append(tupla_comp)
                            messagebox.showinfo('DERROTA', 'O computador ganhou o jogo!')
                            sleep(3)
                            quit()

                        matriz[comp_linha][comp_coluna] = 'O'  # Atualize a matriz com 'O'
                        exibir_matriz()  # Atualize a interface gráfica
                        historico_jogadas.append(tupla_comp)
                    #Fim da jogada do computador
                    pronto_label.config(text="Sua vez")
                    nova_janela.update_idletasks()
                    # Permite a interação com a janela principal
                    nova_janela.grab_release()
                    botao_confirmar.config(state=tk.NORMAL)  # Restaura o estado normal do botão
                    #vai chamar a função computador jogando
                computador_jogando()
    # Fecha a janela atual
    janela.destroy()

    # Cria uma nova janela em branco
    nova_janela = tk.Tk()
    nova_janela.title("Jogo Iniciado")
    nova_janela.geometry("650x450+350+100")

    # Adicione a lógica do jogo à nova janela
    exibir_matriz()
    #crio o campo de entrada p o usu digitar linha e coluna que quer marcar
    label_linha = tk.Label(nova_janela, text='Digite a linha que você quer Marcar')
    label_linha.grid(row=0,column=25)

    label_coluna = tk.Label(nova_janela, text='Digite a coluna que você quer Marcar')
    label_coluna.grid(row=1, column=25)
    linha_tk = tk.Entry(nova_janela)
    coluna_tk = tk.Entry(nova_janela)

    #posiciono os campos de entrada
    linha_tk.grid(row=0, column=30)
    coluna_tk.grid(row=1, column=30)
    #Vou criar o botão para o usuário confirmar o botão que quer jogar
    botao_confirmar = tk.Button(nova_janela, text="Confirmar",width=15, command=validar_dados_e_fazer_jogada)

    botao_confirmar.grid(row=2,column=25)



    # Inicie a interface gráfica da nova janela
    nova_janela.mainloop()


# Função para lidar com o clique no botão "Sair"
def sair():
    janela.quit()

# Criar a janela principal
janela = tk.Tk()
janela.title("Janela-1")

# Definir o tamanho da janela
janela.geometry("650x450+350+100")

# Rótulo de boas-vindas
label = tk.Label(janela, text="Bem-vindo ao Meu Jogo")
label.pack(pady=20)  # Espaço entre o rótulo e os botões

botao_jogar = tk.Button(janela, text="Jogar", command=jogar,width=10)
botao_jogar.pack(pady=10)  # Adicione espaço acima do botão "Jogar"

# Adicione um rótulo vazio para criar espaço vertical
espaco_vazio = tk.Label(janela, text="")
espaco_vazio.pack()

# Botão "Sair"
botao_sair = tk.Button(janela, text="Sair", command=sair,width=10)
botao_sair.pack(pady=10)  # Adicione espaço abaixo do botão "Sair"
# Iniciar a interface gráfica
janela.mainloop()
