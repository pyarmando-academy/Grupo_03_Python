productos = {}
productos_2 = dict()

colores = {
    "yellow": "amarrilo",
    "blue": "azul",
    "black": "negro"
}

valor = colores["blue"]
colores['red'] = "rojo"
colores['red'] = "rojo fuerte"

colores.pop("red")
colores.update({"yellow": "amarillo fuerte"})
print(colores)

clientes = [
    {'cuenta': '2334455', 'apellido': 'Ruiz', 'nombre': 'Armando', 'saldo': 7000},
    {'cuenta': '2334456', 'apellido': 'Gomez', 'nombre': 'Pedro', 'saldo': 8800},
    {'cuenta': '2334457', 'apellido': 'Cespedes', 'nombre': 'Javier', 'saldo': 9000},
    {'cuenta': '2334458', 'apellido': 'Linares', 'nombre': 'Oscar', 'saldo': 12000},
    {'cuenta': '2334459', 'apellido': 'Palomino', 'nombre': 'Maria', 'saldo': 170000}
]

for item in clientes:
    print(item['apellido'])
    print(item['nombre'])
