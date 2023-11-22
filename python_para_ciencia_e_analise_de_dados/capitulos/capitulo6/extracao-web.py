from urllib.request import urlopen
import json

response = urlopen("https://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
dados = json.loads(response)[0]

print("titular: ", dados["title"])
print("URL: ", dados["url"])
print("Duração: ", dados["duration"])
print("Numero de visualizações: ", dados["stats_number_of_plays"])

arquivoFonte = 'capitulos/capitulo6/arquivos/dados.json'
arquivoDestino = 'capitulos/capitulo6/arquivos/dados.json'

with open(arquivoFonte, 'r') as infile:
    text = infile.read()
    with open(arquivoDestino, 'w') as outfile:
        outfile.write(text)