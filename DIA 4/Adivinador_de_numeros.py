from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numero entre 1 y 100\n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1
    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va de 1 a 100")
    elif estimado < numero_secreto:
        print("MI numero es mas ALTO")
    elif estimado > numero_secreto:
        print("MI numero es mas BAJO")
    else:
        print(f"FELICITACIONES... {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto ERA {numero_secreto}")
