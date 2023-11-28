lista = ['a','b','c','d']

for letra in lista:
    print(letra)

#----------------------
lista = ['a','b','c','d']

for letra in lista:
    print("Letra: " + letra)

#-----------------------
lista = ['a','b','c','d']

for letra in lista:
    numero_letras = lista.index(letra) + 1
    print(f"Letra: {numero_letras}: {letra}")
#-----------------------------
lista = ['pablo', 'victor', 'naza', 'sandra','vitoco']

for nombre in lista:
    if nombre.startswith('v'):
        print(nombre)
    else:
        print('Nombre que no comience con V')
#--------------------------
numeros = [1,2,3,4,5,6]
mi_valor = 0

for num in numeros:
    mi_valor = mi_valor + num
print(mi_valor)

#---------------------
palabra = 'python'

for letra in palabra:
    print(letra)

#---------------------
for objeto in [[1,2],[3,4],[10,11]]:
    print(objeto)
#---------------------
for a, b in [[1,2],[3,4],[10,11]]:
    print(a)
    print(b)
#---------------------
dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)

#---------------------
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

suma_pares = 0

suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
