arquivo = open("capitulo6/arquivos/salarios.csv")

data = arquivo.read()
# print(data)
rows = data.split("\n")
fullData = []

for row in rows:
  splitRow = row.split(",")
  fullData.append(splitRow)
  firstRow = fullData[0]
count = 0  

for column in firstRow:
  count = count + 1
  
countRows = 0
for row in fullData:
  countRows += 1

print("Esse é o numero de linhas dentro do arquivo:",countRows) 
print("Esse é o numero de colunas dentro do arquivo:",count) 