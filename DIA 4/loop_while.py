lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break
#----------------------------------

numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

#--------------------------------
numero = 10

while numero >= 0:
    print(numero)
    numero = numero - 1
#-----------------------------------
monedas = 5

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas = monedas - 1
else:print("No hay dinero por mientras")
#----------------------------------------

while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
#--------------------------------------------

respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir? (s/n) ")
else:
    print("Gracias")

#-------------------------------------------
#respuesta = 's'

#while respuesta == 's':
#    pass

#print("hola")
#-------------------------------------------
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#-----------------------------------------
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
#-----------------------------------------


