menor = min(58,96,72,64,30)
mayor = max(58,96,72,64,30)

print(menor)
#-----------------------------------
menor = min(58,96,72,64,30)
mayor = max(58,96,72,64,30)

print(mayor)
#-------------------------------
lista = [58,96,72,64,30]

print(max(lista))
#----------------------------------
lista = [58,96,72,64,30]

print(f'el menor es {min(lista)} y el mayor es {max(lista)}')
#----------------------------------
nombres = ['juan','pablo', 'victor','sandra', 'naza']
print(min(nombres))
print(max(nombres))
#--------------------------------------
nombre = "victor"
print(min(nombre))

nombre = "Victor"
print(min(nombre))

nombre = "Victor"
print(min(nombre.lower()))
#-----------------------------------
dic = {'C1':45,'C2':11}
print(min(dic))

dic = {'C1':45,'C2':11}
print(min(dic.values()))
#ejercicio-------------------
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo =  max(lista_numeros)

#-------------------------------
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)

#-------------------------------
diccionario_edades = {"Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24, "Rocío": 35, "Sebastián": 19,
                      "Catalina": 2, "Darío": 49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())