def suma(a,b):
    return  a+b

print(suma(5,6))

# con args
def sumar(*args):
    total= 0
    for arg in args:
        total += arg
    return total


print(sumar(5,6,7,8,9,2))

#con funcion SUM
def sumado(*args):
    return sum(args)

print(sumado(5,8,79,3,2,23,521))

#ejercicio 1
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2

    return suma

#ejercicio 2
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)

    return suma

#ejercicio 3
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'