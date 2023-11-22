# Criando a lista
x = [1, 2, 3]
y = [4, 5, 6]

zip(x, y)

# Aqui ele vai pegar os itens e mesclar entre as duas listas
lista = list(zip(x, y))

print(lista)

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7]

# Como uma lista tem mais item que a outra, ele vai
# eliminar o item que não formar um par
zip(lista1, lista2)

result = list(zip(lista1, lista2))

print(result)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

list(zip(d1, d2))

def trocaValores(d1, d2):
    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp


trocaValores(d1, d2)

print(trocaValores(d1, d2))

