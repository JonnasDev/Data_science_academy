import csv

with open("capitulos/capitulo6/arquivos/numeros.csv","w") as arquivo:
  writer = csv.writer(arquivo)
  writer.writerow(("nota1","nota2","nota3"))
  writer.writerow((76,309,7))
  writer.writerow((345,627,6))
  writer.writerow((425,875,43))
  
with open("capitulos/capitulo6/arquivos/numeros.csv","r") as arquivo:
  reader = csv.reader(arquivo)
  for leitura in reader:
    print(leitura)
  
  