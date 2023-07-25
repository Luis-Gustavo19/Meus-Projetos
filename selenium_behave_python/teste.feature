#language: pt
Funcionalidade: Consultar a classificação do brasileirão
  '''Como usuário quero entrar na pagina onde mostra a
    tabela do brasileirão e ver a posição de cada time'''

  Cenario: Consultar a tabela do Site GE
    Dado acesso a pagina inicial do globo esporte
    Quando Clico no menu brasileirao
    E classificação e exibida
    Então devo saber os times da tabela