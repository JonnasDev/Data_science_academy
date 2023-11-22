[x for x in range(10)]

listaNumeros = [x for x in range(10)]
print(listaNumeros)

listaFrutas = ["Banana","Maça","Pera","Manga","Uva"]
novaLista = []

for x in listaFrutas:
  if "M" in x:
    novaLista.append(x)

print(novaLista)    

#Comprehension
novaLista = [x for x in listaFrutas if "M" in x]
print(novaLista)