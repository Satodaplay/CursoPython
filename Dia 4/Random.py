from random import *

aleatorio = randint(1, 50)
aleatorioDecimal = uniform(1, 50)
colores = ["azul", "rojo", "verde"]
elejir = choice(colores)
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)
print(aleatorio)