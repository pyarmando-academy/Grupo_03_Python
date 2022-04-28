# for x in range(1,20):
#     print(x)

total = 0
while True:
    producto = input("Ingrese el producto a comprar:")
    precio = float(input("Ingrese el precio del producto:"))
    cant = int(input("Ingrese la cantidad a comprar:"))
    subtotal = precio * cant
    total = total + subtotal #acumulador de susbtotales
    msj = input("Desa Seguir comprando:(s/n)")
    if msj == "N":
        print("El Total a pagar es", total)
        break  # False


