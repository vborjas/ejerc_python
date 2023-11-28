mi_lista = ['a','b','c']
resultado = len(mi_lista)
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[1]
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0:]
print(resultado)

mi_lista = ['a','b','c']
resultado = mi_lista[0:2]
print(resultado)


mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
resultado = mi_lista+mi_lista2
print(resultado)

#CAMBIAR UN ELEMENTO DIRECTO SIN GUARDAR
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
print(mi_lista3)

mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
mi_lista3.pop()
print(mi_lista3)

#agregar un elemento a la lista con append
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
mi_lista3.pop(1)
print(mi_lista3)

#eliminar con POP y guardar lo elimiando en una variable
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
eliminado = mi_lista3.pop(1)
print(mi_lista3)
print(eliminado)

#ORDENAR LISTA
lista =  ['g', 'o', 'b', 'm', 'c']
lista.sort()
print(lista)

#invertir el orden
lista =  ['g', 'o', 'b', 'm', 'c']
lista.reverse()
print(lista)



