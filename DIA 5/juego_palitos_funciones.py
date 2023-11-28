from random import shuffle
# lista inicial
palitos = ['-', '--', '---', '----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista
# print(mezclar(palitos))-- probar que mezcla

# pedirle intentos
def probar_suerte():
    intento =  ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4:_ ")
    return int(intento)
''' 
comprobacion de codigo
intento1 = probar_suerte()
print(intento1)
'''
# comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print(("A LAVAR LOS PLATOS"))
    else:
        print("ESTA VEZ TE SALVASTE")
    print(f"te ha tocado {lista[intento-1]}")

# final
palitos_mexclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mexclados, seleccion)

