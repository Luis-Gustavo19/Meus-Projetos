from rembg import remove
from PIL import Image
import os

pasta_entrada = "C:\DEV\mbientelivre\pasta1"
pasta_saida = "C:\DEV\mbientelivre\pasta2"

num_arquivos = len(os.listdir(pasta_entrada))
num_arquivos_saida = len(os.listdir(pasta_saida))

for i, nome_arquivo in enumerate(sorted(os.listdir(pasta_entrada))):
    if nome_arquivo.endswith(".jpg"):
        nome_antigo = os.path.join(pasta_entrada, nome_arquivo)
        nome_novo = os.path.join(pasta_entrada, f"{i}.jpg")
        os.rename(nome_antigo, nome_novo)

for i in range(num_arquivos):
    input_path = f"{pasta_entrada}/{i}.jpg"
    output_path = f"{pasta_saida}/{i + num_arquivos_saida}.png"

    # Verificar se o arquivo de saída com o mesmo índice já existe
    if os.path.exists(output_path):
        continue  # Pular para o próximo índice disponível

    entrada_imagem = Image.open(input_path)
    saida_imagem_sem_fundo = remove(entrada_imagem)
    saida_imagem_sem_fundo.save(output_path)
    os.remove(input_path)
