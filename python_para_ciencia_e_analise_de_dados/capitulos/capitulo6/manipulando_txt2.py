# O metodo WITH fecha o arquivo automaticamente
with open("capitulos/capitulo6/arquivos/cientista.txt", "r") as arquivo:
  conteudo = arquivo.read()
  
print(len(conteudo))
print(conteudo)  


  