texto = "Este es un texto de Victor"

resultado = texto.upper()

print(resultado)


texto = "Este es un texto de Victor"

resultado = texto[2].upper()

print(resultado)


texto = "Este es un texto de Victor"

resultado = texto.lower()

print(resultado)


texto = "Este es un texto de Victor"

resultado = texto.split()

print(resultado)


texto = "Este es un texto de Victor"

resultado = texto.split("t")

print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)


texto = "Este es un texto de Victor"

resultado = texto.find("e")

print(resultado)


texto = "Este es un texto de Victor"

resultado = texto.replace("Victor", "Victorius")

print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil" , "facil" )
x = resultado.replace("mala","buena")


print(x)