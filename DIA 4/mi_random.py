from random import *
aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5),2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

numero = list(range(5,50,5))
shuffle(numero)
print(numero)