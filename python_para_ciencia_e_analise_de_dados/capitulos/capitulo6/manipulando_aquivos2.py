# Abrindo arquivo para escrita, sobrescrevendo o arquivo, caso ele não exista, sera criado
arquivo2 = open("capitulo6/arquivos/nada_escrito_aqui_2.txt", "w")

# Abrindo arquivo existente e adicionando caracteres
arquivo2 = open("capitulo6/arquivos/nada_escrito_aqui_2.txt", "a")  #Append

# Gravando no arquivo
arquivo2.write("Ola mundo")

# Fechando o arquivo
arquivo2.close()

# Abrindo arquivo de novo para leitura
arquivo2 = open("capitulo6/arquivos/nada_escrito_aqui_2.txt", "r")

print(arquivo2.read())