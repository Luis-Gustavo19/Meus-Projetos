import pygame
import random
import threading
import math
import os
import sys
from time import sleep # Adicionado para lidar com a pausa
script_dir = os.path.abspath(os.path.dirname(__file__))
#Tela onde o jogador escolhe a velocidade
#itens de jogo que tem que ser global
municao =30
terminou_a_func = True
game_over = False
'''  "ESPAÇO" Para atirar E "F" para o especial'''
def recarregando(s=2):
    global terminou_a_func
    global municao
    terminou_a_func = False
    sleep(s)
    municao =30
    terminou_a_func =True


tempo_limite_segundos = 120 # 2 minuto


# Inicialize o Pygame
pygame.init()

#função que complementa na onda ali
def distancia(ponto1, ponto2):
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
#efeitos musicais do lobby
botaosound = pygame.mixer.Sound(os.path.join(script_dir, 'audio/botaosound.mp3'))
pygame.mixer.music.load('audio/audio_tela1.mp3')
pygame.mixer.music.play()

# Defina as dimensões da tela e crie a tela
largura_tela_loby = 800
altura_tela_loby = 600
tela = pygame.display.set_mode((largura_tela_loby, altura_tela_loby))

# Carregue a imagem de fundo
imagem_fundo_loby = pygame.image.load(os.path.join(script_dir, 'img/lobby.png')).convert()
imagem_fundo_loby= pygame.transform.scale(imagem_fundo_loby, (largura_tela_loby, altura_tela_loby))

# Defina as cores
cor_titulo = (255, 255, 255)  # Vermelho

# Defina a fonte e crie objetos de texto
fonte_titulo_loby = pygame.font.Font(None, 72)
titulo = fonte_titulo_loby.render("Invasão Cósmica", True, cor_titulo)

# Posicionamento do título
posicao_titulo = ((largura_tela_loby - titulo.get_width()) // 2, 100)

# Defina as cores dos botões
cor_facil = (72, 167, 153)  # Verde
cor_medio = (12, 33, 28)  # Verde escuro
cor_dificil = (44, 104, 96)  # Verde claro

# Crie retângulos para os botões
retangulo_facil = pygame.Rect((largura_tela_loby // 2 - 100, 300, 200, 50))
retangulo_medio = pygame.Rect((largura_tela_loby // 2 - 100, 370, 200, 50))
retangulo_dificil = pygame.Rect((largura_tela_loby // 2 - 100, 440, 200, 50))

# Loop principal do lobby
lobby_ativo = True
while lobby_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lobby_ativo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            #se escolher o nivel fácil
            if retangulo_facil.collidepoint(x, y):
                botaosound.play()
                lobby_ativo = False  # Adicione a lógica desejada para começar o jogo no modo FÁCIL
                velo_nivel =8
                velo_inimigo_nivel = 1
                velo_tiro_inimigo = 3
            #se escolher o nivel médio
            elif retangulo_medio.collidepoint(x, y):
                botaosound.play()
                velo_nivel = 7
                velo_inimigo_nivel = 2
                velo_tiro_inimigo = 5
                lobby_ativo = False  # Adicione a lógica desejada para começar o jogo no modo MÉDIO
             #se escolher o nivel dificl
            elif retangulo_dificil.collidepoint(x, y):
                botaosound.play()
                velo_nivel = 7
                velo_inimigo_nivel = 2
                velo_tiro_inimigo = 8
                lobby_ativo = False  # Adicione a lógica desejada para começar o jogo no modo DIFÍCIL

    # Desenhe a imagem de fundo
    tela.blit(imagem_fundo_loby, (0, 0))

    # Desenhe elementos na tela
    tela.blit(titulo, posicao_titulo)

    # Desenhe os botões
    pygame.draw.rect(tela, cor_facil, retangulo_facil)
    pygame.draw.rect(tela, cor_medio, retangulo_medio)
    pygame.draw.rect(tela, cor_dificil, retangulo_dificil)

    # Adicione textos aos botões
    fonte_botoes = pygame.font.Font(None, 36)
    texto_facil = fonte_botoes.render("FÁCIL", True, (255, 255, 255))
    texto_medio = fonte_botoes.render("MÉDIO", True, (255, 255, 255))
    texto_dificil = fonte_botoes.render("DIFÍCIL", True, (255, 255, 255))

    tela.blit(texto_facil, (largura_tela_loby// 2 - texto_facil.get_width() // 2, 315))
    tela.blit(texto_medio, (largura_tela_loby // 2 - texto_medio.get_width() // 2, 385))
    tela.blit(texto_dificil, (largura_tela_loby // 2 - texto_dificil.get_width() // 2, 455))

    pygame.display.update()

# Aguarde alguns segundos antes de encerrar
pygame.mixer.music.stop()
pygame.time.wait(3000)


# Carregar o som efeitos do game
tiro_sound = pygame.mixer.Sound(os.path.join(script_dir, 'audio/laser.mp3'))
explosion_sound = pygame.mixer.Sound(os.path.join(script_dir, 'audio/explosion.mp3'))
game_over_sound = pygame.mixer.Sound(os.path.join(script_dir, 'audio/gameover.mp3'))
lista_de_musicas = [os.path.join(script_dir, 'audio/musica1.mp3'), os.path.join(script_dir, 'audio/musica2.mp3'), os.path.join(script_dir, 'audio/musica3.mp3'), os.path.join(script_dir, 'audio/musica4.mp3')]

musica_princ =pygame.mixer.Sound(random.choice(lista_de_musicas))
vitoria_sound = pygame.mixer.Sound(os.path.join(script_dir, 'audio/vitoria_sound.mp3'))

# Função para criar um novo inimigo
def criar_inimigo():
    imagem_inimigo = pygame.image.load(os.path.join(script_dir, 'img/inimigo_nave.png')).convert_alpha()
    imagem_inimigo = pygame.transform.scale(imagem_inimigo, (50, 50))

    largura_inimigo = 50  # Largura da imagem do inimigo
    altura_inimigo = 50  # Altura da imagem do inimigo

    posicao_inimigo = [random.randint(0, largura_tela - largura_inimigo), -altura_inimigo]  # Inimigo aparece acima da tela
    velocidade_inimigo = velo_inimigo_nivel  # Velocidade escolhida no nivel

    return {"imagem": imagem_inimigo, "posicao": posicao_inimigo, "velocidade": velocidade_inimigo}
# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela e crie a tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Carregue a imagem de fundo
imagem_fundo = pygame.image.load(os.path.join(script_dir, 'img/espaco.jpg')).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

# Carregue a imagem da nave
imagem_nave = pygame.image.load(os.path.join(script_dir, 'img/nave.png')).convert_alpha()
imagem_nave = pygame.transform.scale(imagem_nave, (50, 50))

# Lista para armazenar inimigos
inimigos = []

# Lista para armazenar os tiros do jogador
tiros_jogador = []

# Lista para armazenar os tiros dos inimigos
tiros_inimigos = []

# Cores dos tiros
cor_tiro_jogador = (255, 255, 0)  # Amarelo
cor_tiro_inimigo = (255, 0, 0)  # Vermelho

# Posição inicial da nave
posicao_nave = [largura_tela // 2, altura_tela - 60]  # Posicionada no centro inferior

# Velocidade de movimento da nave
velocidade_nave = velo_nivel

# Controle de disparo do jogador
pode_atirar_jogador = True

# Controle de disparo dos inimigos
pode_atirar_inimigo = [True] * 10  # Cada inimigo tem seu próprio controle de disparo

# Controle de game over
game_over = False

# Defina a fonte e crie um objeto de texto
fonte = pygame.font.Font(None, 36)  # Escolha a fonte e o tamanho desejados
score = 0
texto_score = fonte.render(f'Score: {score}', True, (255, 255, 255))  # Cor branca

# Defina a posição do texto
posicao_score = (20, 20)  # Ajuste conforme necessário

# Clock do Pygame, que é usado para controlar a velocidade do jogo
clock = pygame.time.Clock()
#painel
cor_retangulo = (0, 68, 83)
cor_texto = (255,255,255)
cor_texto_bran = (255, 255, 255)
cor_texto_verme = (255, 0, 0)
cor_texto_laran = (255, 165, 0)
cor_texto_verde = (0, 128, 0)



imagem_jogador = pygame.image.load(os.path.join(script_dir, "img/navebranca.png"))
imagem_jogador = pygame.transform.scale(imagem_jogador, (50, 50))
fonte = pygame.font.Font(None, 36)

imagem_laser = pygame.image.load(os.path.join(script_dir, 'img/laser.png')).convert_alpha()
imagem_laser = pygame.transform.scale(imagem_laser, (10, 30))  # Ajuste o tamanho conforme necessário

imagem_laser_inimigo = pygame.image.load(os.path.join(script_dir, 'img/laserinimigo.png')).convert_alpha()
imagem_laser_inimigo = pygame.transform.scale(imagem_laser_inimigo, (7, 25))  # Ajuste o tamanho conforme necessário

# Lógica da onda
onda_usada = False
max_usos_onda = 5 # Defina o número máximo de usos da onda desejado
usos_onda = 0
velocidade_onda = -900
onda_ativa = False
onda_radius = 0
max_onda_radius = 800
growth_factor = 5
onda_som = pygame.mixer.Sound(os.path.join(script_dir, 'audio/eletricSound.mp3'))

shock_factor = 2


def desenhar_hud(muni=municao, vida=1):
    global usos_onda
    usos_onda
    # Ajusta as coordenadas para um pequeno retângulo no canto superior direito
    largura_painel = 215
    altura_painel = 100
    x_painel = largura_tela - largura_painel
    y_painel = 0
    # Garante que o retângulo não ultrapasse os limites da tela
    x_painel = max(1, min(x_painel, (largura_tela-0) - largura_painel-0))

    pygame.draw.rect(tela, cor_retangulo, (x_painel, y_painel, largura_painel, altura_painel))
    tela.blit(imagem_jogador, (x_painel + 10, y_painel + 10))
    if municao <=30:
        texto_municao = fonte.render(f"Munição: {municao}", True, cor_texto_verde)
    if municao <=20:
        texto_municao = fonte.render(f"Munição: {municao}", True, cor_texto_laran)
    if municao<=10:
        texto_municao = fonte.render(f"Munição: {municao}", True, cor_texto_verme)

    if usos_onda <=2:
        texto_onda = fonte.render(f"Power: {usos_onda}/5", True, cor_texto_verde)
    if usos_onda >=2 or usos_onda==4:
        texto_onda = fonte.render(f"Power: {usos_onda}/5", True, cor_texto_laran)
    if usos_onda >=5:
        texto_onda = fonte.render(f"Power: {usos_onda}/5", True, cor_texto_verme)

    tela.blit(texto_municao, (x_painel + 70, y_painel + 10))
    tela.blit(texto_onda, (x_painel + 70, y_painel + 40))


    texto_vida = fonte.render(f"Vida: {vida}", True, cor_texto)
    tela.blit(texto_vida, (x_painel + 70, y_painel + 70))


vitoria = False
# Loop principal do jogo
repetir_musica = 0
tempo_inicial = pygame.time.get_ticks() // 1000 # Tempo em segundos
tempo_atual = (pygame.time.get_ticks() // 1000) - tempo_inicial
while not game_over:
    if repetir_musica ==0:
        musica_princ.play(loops=-1)
        repetir_musica+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f] and not onda_ativa and not onda_usada and usos_onda < max_usos_onda:
        onda_ativa = True
        onda_usada = True
        usos_onda += 1
        onda_som.play()
        velocidade_onda = 2  # Reinicia a velocidade da onda ao ativar

    if onda_ativa:
        # Desenha o plano de fundo
        tela.blit(imagem_fundo, (0, 0))

        # Remove inimigos atingidos pela onda
        inimigos = [inimigo for inimigo in inimigos if
                    distancia(tuple(inimigo["posicao"]), tuple(posicao_nave)) > onda_radius]

        # Desenha a nave na tela
        tela.blit(imagem_nave, tuple(posicao_nave))

        # Desenha os inimigos na tela
        for inimigo in inimigos:
            tela.blit(inimigo["imagem"], tuple(inimigo["posicao"]))

        # Desenha o painel
        desenhar_hud()

        # Desenha a aura
        pygame.draw.circle(tela, (0, 0, 255), tuple(posicao_nave), onda_radius, 2)

        # Atualiza a tela
        pygame.display.update()

        # Atualiza o raio da onda com a velocidade ajustada
        onda_radius += velocidade_onda
        velocidade_onda += growth_factor
        growth_factor += shock_factor

        # Atualiza os inimigos e os tiros dos inimigos (como antes)

        # Verifica se a onda atingiu seu tamanho máximo
        if onda_radius >= max_onda_radius:
            onda_ativa = False
            onda_radius = 0
            onda_usada = False
            velocidade_onda = 2  # Reinicia a velocidade da onda

        # Crie novos inimigos se houver menos de 10 na tela
    if len(inimigos) < 10 and random.randint(0, 100) < 5:
        inimigos.append(criar_inimigo())

    if not game_over:
        # Verifique as teclas pressionadas para mover a nave e atirar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and posicao_nave[0] > 0:
            posicao_nave[0] -= velocidade_nave
        if keys[pygame.K_RIGHT] and posicao_nave[0] < largura_tela - 50:
            posicao_nave[0] += velocidade_nave

        if keys[pygame.K_SPACE] and pode_atirar_jogador:
            if municao >0 and terminou_a_func == True:
                municao -=1
                tiro_sound.play()

            if municao ==0 and terminou_a_func == True:
                pode_atirar_jogador = False
                thread = threading.Thread(target=recarregando).start()

            # Adicione um novo tiro do jogador à lista de tiros
            posicao_tiro_jogador = posicao_nave.copy()
            posicao_tiro_jogador[0] += 25  # Ajuste para o centro da nave

            tiros_jogador.append({"posicao": posicao_tiro_jogador.copy(), "imagem": imagem_laser, "velocidade": 5})
            pode_atirar_jogador = False  # Desativar disparo temporariamente logo não mexe nele, deixa como está

        # Controle de disparo para evitar múltiplos tiros contínuos
        if not keys[pygame.K_SPACE]:
            if municao ==0:
                pode_atirar_jogador = False
            else:
                pode_atirar_jogador = True

        # Crie novos tiros dos inimigos em intervalos
        for i, inimigo in enumerate(inimigos):
            if random.randint(0, 100) < 2 and pode_atirar_inimigo[i]:
                tiros_inimigos.append({"posicao": inimigo["posicao"].copy(), "imagem": imagem_laser_inimigo,
                                       "velocidade": velo_tiro_inimigo})

                pode_atirar_inimigo[i] = False  # Desativar disparo temporariamente


        # Controle de disparo dos inimigos para evitar múltiplos tiros contínuos
        for i in range(10):
            if not any(tiro["posicao"][1] < altura_tela for tiro in tiros_inimigos):
                pode_atirar_inimigo[i] = True

        # Atualize a posição dos inimigos e remova aqueles que saíram da tela
        for inimigo in inimigos:
            inimigo["posicao"][1] += inimigo["velocidade"]
            inimigo["posicao"][0] += random.choice([-1, 1])
            if inimigo["posicao"][1] > altura_tela:
                game_over = True

        # Atualize a posição dos tiros do jogador e remova aqueles que saíram da tela
        for tiro in tiros_jogador:
            tiro["posicao"][1] -= tiro["velocidade"]
            if tiro["posicao"][1] < 0:
                tiros_jogador.remove(tiro)

        # Atualize a posição dos tiros dos inimigos e remova aqueles que saíram da tela
        for tiro in tiros_inimigos:
            tiro["posicao"][1] += tiro["velocidade"]
            if tiro["posicao"][1] > altura_tela:
                tiros_inimigos.remove(tiro)

        # Verifique colisões com os tiros do jogador
        for tiro in tiros_jogador:
            for inimigo in inimigos:
                if (
                    inimigo["posicao"][0] < tiro["posicao"][0] < inimigo["posicao"][0] + 50
                    and inimigo["posicao"][1] < tiro["posicao"][1] < inimigo["posicao"][1] + 50
                ):
                    explosion_sound.play()
                    inimigos.remove(inimigo)
                    tiros_jogador.remove(tiro)
                    score += 1

        for inimigo in inimigos:
            if distancia(tuple(inimigo["posicao"]), tuple(posicao_nave)) > onda_radius:
                continue

            # Se a nave inimiga foi atingida pela onda
            explosion_sound.play()
            inimigos.remove(inimigo)
            # Adicione pontuação quando uma nave inimiga é abatida

        # Verifique colisões com os tiros dos inimigos
        for tiro in tiros_inimigos:
            if (
                posicao_nave[0] < tiro["posicao"][0] < posicao_nave[0] + 50
                and posicao_nave[1] < tiro["posicao"][1] < posicao_nave[1] + 50
            ):
                game_over = True

        # Verifique colisões com as naves inimigas
        for inimigo in inimigos:
            if (
                posicao_nave[0] < inimigo["posicao"][0] < posicao_nave[0] + 50
                and posicao_nave[1] < inimigo["posicao"][1] < posicao_nave[1] + 50
            ):
                game_over = True

        # Desenhe a imagem de fundo na tela
        tela.blit(imagem_fundo, (0, 0))

        # Desenhe a nave na tela
        tela.blit(imagem_nave, tuple(posicao_nave))

        # Desenhe os inimigos na tela
        for inimigo in inimigos:
            tela.blit(inimigo["imagem"], tuple(inimigo["posicao"]))

        # Desenhe os tiros na tela
        for tiro in tiros_jogador:
            tela.blit(tiro["imagem"], (int(tiro["posicao"][0]), int(tiro["posicao"][1])))

        for tiro in tiros_inimigos:
            tela.blit(tiro["imagem"], (int(tiro["posicao"][0]), int(tiro["posicao"][1])))

        # Atualize o score
        texto_score = fonte.render(f'Score: {score}', True, (255, 255, 255))
        tempo_atual = (pygame.time.get_ticks() // 1000) - tempo_inicial

        texto_tempo = fonte.render(f'Tempo:{tempo_atual}/120',True,(255,255,255))
        # Desenhe o texto do score na tela
        tela.blit(texto_score, posicao_score)
        tela.blit(texto_tempo,(20,50))
        desenhar_hud()
        if tempo_atual >= tempo_limite_segundos:
            vitoria =True
            break

        # Atualize a tela
        pygame.display.update()



        # Controle de frames por segundo
        clock.tick(30)
if game_over == True:
    musica_princ.stop()
    # Game over: tela escura e mensagem
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    game_over_sound.play()
    mensagem_game_over = fonte.render('    Game Over''\n'f'Sua Pontuação: {score}', True, (255, 255, 255))
    posicao_mensagem = (
        (largura_tela - mensagem_game_over.get_width()) // 2,
        (altura_tela - mensagem_game_over.get_height()) // 2,
    )
    tela.blit(mensagem_game_over, posicao_mensagem)
    pygame.display.update()

    # Aguarde alguns segundos antes de encerrar
    pygame.time.wait(3000)
    pygame.quit()

if vitoria:
    musica_princ.stop()
    # Defina as dimensões da tela
    largura_tela = 800
    altura_tela = 600

    # Crie a tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Carregue a imagem de fundo
    imagem_fundo_vitoria = pygame.image.load(os.path.join(script_dir, 'img/vito2.jpg'))
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

    # Defina a posição da imagem na tela
    posicao_imagem = (0,0)  # Ajuste conforme necessário
    vitoria_sound.play()
    # Exiba a imagem de fundo na tela
    tela.blit(imagem_fundo, posicao_imagem)
    pygame.display.update()

    # Aguarde 3 segundos
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

