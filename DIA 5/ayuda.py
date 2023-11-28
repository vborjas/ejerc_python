
letras = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
elimina = letras.lstrip(',:%_#')
print(elimina)
#---------------------------------------------------

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "Naranja")
print(frutas)
#----------------------------------------------
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

#------------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"hola", "microsoft", "carro"}
z = x.isdisjoint(y)
print(z)