import json

with open ("capitulos/capitulo6/arquivos/dados.json","r") as arquivo:
  leitor = arquivo.read()
  dados = json.loads(leitor)
  print(dados) 

  