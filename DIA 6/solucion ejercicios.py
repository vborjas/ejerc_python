#practica de archivo 1

archivo = open("texto.txt")
print(archivo.read())

#practica de archivo 2

mi_archivo = open("texto.txt")
print(mi_archivo.readline())

#practica de archivo 3
archivo = open("texto.txt")
lineas = archivo.readlines()
print(lineas[1])

# Alternativa de solución admitida:
# lineas = archivo.readline()
# lineas = archivo.readline()
# print(lineas)

#practica de archivo escribir 1

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#practica de archivo escribir 2

archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#practica de archivo escribir 3

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + '\t')

registro.close()
registro = open("registro.txt", "r")
print(registro.read())