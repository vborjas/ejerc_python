##caso antiguo 3.09
serie = "N-02"
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("NO Existe el producto")

##nuevo uso del MATCH en version 3.10

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe Producto")

#-------------------------
cliente = {'nombre':'federico',
           'edad': 45,
           'ocupacion': 'instructor'}
pelicula = {'titulo': 'matrix',
            'ficha_tecnica':{'protagonista': 'Keanu reeves',
                             'director': 'Lana y Lilly Wachowski'}}
elemento = [cliente, pelicula, 'libro']

for e in elemento:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica':{'protagonista': protagonista,
                               'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")