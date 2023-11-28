if 10 > 9:
    print('es correcto')

#----------
x = True
if x:
    print('Es correcto')
#----------
if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

#-----------
mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal Tienes')
#------------------------
edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de Edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No Aprobado')
else:
    print('Eres Adulto')
#---------------------------
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num1 == num2:
    print(f'{num1} y {num2} son iguales')
elif num2 > num1:
    print(f'{num2} es mayor que {num1}')

#-----------------------------
edad = 16
tiene_licencia = False

if edad >= 18:
    print("Puedes conducir")
    if tiene_licencia == True:
        print("Puedes conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

#---------------------------------
habla_ingles = True
sabe_python = False

if (habla_ingles == True) and (sabe_python == True):
    print("Cumples con los requisitos para postularte")
elif (habla_ingles == False) and (sabe_python ==  False):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif (habla_ingles == False) and (sabe_python == True):
    print("Para postularte, necesitas tener conocimientos de inglés")
elif (habla_ingles == True) and (sabe_python == False):
    print("Para postularte, necesitas saber programar en Python")







