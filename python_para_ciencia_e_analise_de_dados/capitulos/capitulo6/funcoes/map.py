def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
numerosAoQuadrado = list(map(potencia, numeros))
print(numerosAoQuadrado)

def fahrenheit(T):
    return ((float(9) / 5) * T + 32)
def celcius(T):
    return ((float(5) / 9) * (T - 32))


temperaturas = [0, 23.5, 40, 100]

resultF = list(map(fahrenheit, temperaturas))
print("Resultado em fahrenheit", resultF)

resultC = list(map(celcius, temperaturas))
print("Resultado em celsius: ", resultC)


map(lambda x: (5.0/9)*(x - 32), temperaturas)
a = [1,2,3,4]
b = [5,6,7,8]

list(map(lambda x,y:x*y,a,b))