# if "TECLADO" in mis_productos:
#     print("Producto hallado")
# else:
#     print("Product no localizado")

# productos = ["COMPUTADOR", "IMPRESORA", "TECLADO", "PARLANTE", "MONITOR"]
# precios = [1200, 300, 20, 12, 50]
# stock = [20, 56, 12, 45, 13]

mis_productos = {"COMPUTADOR": 1200, "INPRESORA": 300, "TECLADO": 20, "PARLANTE": 12, "MONITOR": 50}

mi_lista = []
tot = 0
while True:
    prod = input("Ingrese el Nombre del producto:")
    if prod in mis_productos:
        cant = int(input("Ingrese la cantidad a comprar:"))
        pre = mis_productos[prod]
        mi_lista.append(prod)
        subtotal = pre * cant
        tot = tot + subtotal
        msg = input("Desea Continuar con la compra(s/n)")
        if msg == "N":
            print(mi_lista)
            print(f'El Total de su compra es {tot}')
            break
