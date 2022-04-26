productos = []
clientes = list()

frutas = ['banana', 'naranjas', 'fresas', 'manzana']

# todo imprimiendo la lista
# print(frutas)
# todo recorriendo la  lista
# for fruta in frutas:
#     print(fruta)

# todo accediento a un elemnto de la lista
# print(frutas[2])
# print(frutas[1:3])
# print(frutas[1:])
# print(frutas[-3:-1])

# todo funcion index me devuelve la posicion del elemento en la lista
# print(frutas.index('fresas'))

# todo me permite buscar un elemento en la lista
# if 'banana' in frutas:
#     print("La Fruta existe en la lista")
# else:
#     print("La Fruta no existe en la lista")

# todo insertar elementos a la lista
frutas.append("sandia")
frutas.insert(2, "uvas")

# todo eliminar elementos de la lista
frutas.pop(0)
frutas.remove("naranjas")

# todo modificar elementos de la lista
frutas[0] = "maracuya"

# todo ordenar las listas
# frutas.sort()
frutas.reverse()

# todo elimina todo el contenido de la lista
# frutas.clear()
# todo hacer una copia de la lista
backup_frutas = frutas.copy()
vegetales = ["tomate", "col", "brocoli"]
frutas_vegetales = backup_frutas + vegetales
backup_frutas.extend(vegetales)

# todo contar elementos de la lista
tamaño = len(backup_frutas)
# tamaño = backup_frutas.count('banana')

clientes = ["armando", 20, 23.56, True, [12, 56, 78]]

# todo crear un programa que me permita llevar el inventario de una tienda
# todo de zapatos

productos = [
    {"codigo": "A100", "nombre": "zapato mujer", "precio": 200, "stock": 100},
    {"codigo": "A200", "nombre": "zapato caballero", "precio": 50, "stock": 80},
    {"codigo": "A300", "nombre": "zapato niños", "precio": 70, "stock": 30},
    {"codigo": "A400", "nombre": "zapatos de futbol", "precio": 80, "stock": 10},
]

codigo_busqueda = input("Ingrese el codigo del producto:")
encontrar = False
for item in productos:
    if codigo_busqueda == item['codigo']:
        encontrar = True
        print(f"Nombre : {item['nombre']} Precio {item['precio']}")
        break
if encontrar == False:
    print("no se encontro el producto")
