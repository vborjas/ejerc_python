a = 10
b = 5
c = 15

mi_bool = 4 < 5 < 6
print(mi_bool)
#AND
mi_bool = (4 < 5) and (5 > 2+3)
print(mi_bool)

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

#OR
mi_bool = (4 < 5) or (5 > 2+3)
print(mi_bool)

texto = "esta frase es breve"
mi_bool =( 'frase' in texto) or ('breve' in texto)
print(mi_bool)

#NOT
mi_bool = not ('a' == 'a')
print(mi_bool)()