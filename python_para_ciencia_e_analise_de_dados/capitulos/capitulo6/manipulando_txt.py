import os

arquivo = open(os.path.join("capitulos/capitulo6/arquivos/cientista.txt"),"w")

texto = "Cientista de dados do Brasil "
texto += "Estão em deficit"

for palavra in texto.split():
  arquivo.write(palavra + " ")
  
arquivo.close()

arquivo = open(os.path.join("capitulos/capitulo6/arquivos/cientista.txt"),"r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

  