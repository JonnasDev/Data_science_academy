# Abrindo o arquivo para leitura
f = open("capitulo6/arquivos/salarios.csv", "r")

# Salvando a função de abertura dentro de uma variavel
data = f.read()

# Usando o split para poder para tirar a função "\n" do arquivo
rows = data.split("\n")

print(rows)
print("\n-----------------------------")

fullData = [] # Criando uma lista vazia

# Dividindo cada item da coluna por objeto
for row in rows:
  splitRow = row.split(",")
  fullData.append(splitRow)
print(fullData) 