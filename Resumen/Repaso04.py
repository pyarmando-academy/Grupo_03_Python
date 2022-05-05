"""
Escribir un programa que cree un diccionario simulando
una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de
la compra y el coste total, con el siguiente formato
"""
cesta = {}
continuar = True
while continuar:
    item = input("Introduce un Articulo:")
    precio = float(input("Introduce el precio de " + item + ":"))
    cesta[item] = precio
    continuar = input("¿Quieres añadir mas articulos a tu cesta (SI/NO)?") == "Si"
costo = 0
print("Lista de la compra")
for item, precio in cesta.items():
    print(item, '\t', precio)
    costo += precio
print("Costo total es", costo)

# cesta = {"Televisor": 1200, "Laptop": 800}
