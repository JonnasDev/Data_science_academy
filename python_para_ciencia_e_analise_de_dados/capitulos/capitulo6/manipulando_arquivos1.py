 #Abrindo o arquivo para leitura
arquivo = open("capitulo6/arquivos/nada_escrito_aqui.txt", "r")

# Lendo o arquivo
print(arquivo.read())

# Contar o numero de caracteres no arquivo
print(arquivo.tell())

# Retornar para o inicio do arquivo
print(arquivo.seek(0,0))

# Lendo os primeiros 10 caracteres
print(arquivo.read(10))