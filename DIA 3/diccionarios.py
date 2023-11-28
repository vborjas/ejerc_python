diccionario = {'c1':'valor1', 'c2':'valor2'}
print(diccionario)

resultado = diccionario['c2']
print(resultado)

cliente = {'nombre':'juan', 'apellido':'Fuentes','peso':88, 'talla':1.76}
consulta = (cliente['talla'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200} }
print(dic['c2'])

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200} }
print(dic['c2'][1])

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200} }
print(dic['c3']['s2'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

dic = {1:'a', 2:'b'}
print(dic)
dic[3]= 'c'
print(dic)


dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])