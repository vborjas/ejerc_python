def multiplicar(numero1,numero2):
    return numero1 * numero2

print(multiplicar(5,10))

#------------------------------------------------
def multiplicar(numero1,numero2):
    return numero1 * numero2

resultado = multiplicar(5,200)
print(resultado)
#---------------------------------------------
def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

total = multiplicar(10,200)
print(total)
#---------------------------------------------
def potencia(arg1,arg2):
    resultado = arg1**arg2
    return resultado

#------------------------------
def usd_a_eur(valor1):
    conversion = valor1*0.90
    return conversion

dolares = usd_a_eur(50)
print(dolares)
#---------------------------------
dolares = 1200
def usd_a_eur(dolares):
    return dolares * 0.90
#---------------------------------
palabra = "Curso de Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
print(invertir_palabra(palabra))