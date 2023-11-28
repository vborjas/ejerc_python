nombres = ['ana','hugo','valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinado = list(zip(nombres,edades,ciudades))
print(combinado)

for nombre, edad, ciudad in combinado:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

#----------------------------------------
marcas = ['nike', 'adidas','puma', 'sckiker']
productos =['zapato deportivo', 'zapato para correr', 'zapato para futbol', 'zapato para joven']

mi_zip = zip(marcas,productos)
#-----------------------------------------
espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))