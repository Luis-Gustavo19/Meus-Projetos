from rembg import remove
from PIL import Image
import os

pasta_entrada = "add caminho"
pasta_saida = "add caminho"

# Renomear os arquivos da pasta de entrada
num_arquivos = len(os.listdir(pasta_entrada))
print(num_arquivos)
for i, nome_arquivo in enumerate(sorted(os.listdir(pasta_entrada))):
    if nome_arquivo.endswith(".jpg"):
        nome_antigo = os.path.join(pasta_entrada, nome_arquivo)
        nome_novo = os.path.join(pasta_entrada, f"{i}.jpg")
        os.rename(nome_antigo, nome_novo)

# Processar as imagens renomeadas
for i in range(num_arquivos):
    input_path = os.path.join(pasta_entrada, f"{i}.jpg")
    output_path = os.path.join(pasta_saida, f"{i}.png")
    if os.path.exists(output_path) ==True:
        a = 0
        while os.path.exists(output_path) ==True:
            a+=1
            output_path = os.path.join(pasta_saida, f"{a}.png")

    entrada_imagem = Image.open(input_path)
    saida_imagem_sem_fundo = remove(entrada_imagem)
    saida_imagem_sem_fundo.save(output_path)
    os.remove(input_path)
