num1 = 20
num2 =  30.5

print(type(num1))
print(type(num2))

#conversion implicita lo hace automaticamente
num1 = num1 + num2
print(type(num1))
print(type(num2))

#conversion explicita lo hace automaticamente
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu Edad:  ")
print(type(edad))

edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)