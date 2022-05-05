"""
Escribir un programa que gestione las facturas pendientes de cobro de
una empresa. Las facturas se almacenarán en un diccionario donde la
clave de cada factura será el número de factura y el valor el coste de
la factura. El programa debe preguntar al usuario si quiere añadir una
nueva factura, pagar una existente o terminar. Si desea añadir una nueva
factura se preguntará por el número de factura y su coste y se añadirá
al diccionario. Si se desea pagar una factura se preguntará por el número
de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la cantidad cobrada hasta el
 momento y la cantidad pendiente de cobro.
"""

# T=continuar , A=Añadir , P ='Pagar'
facturas = {}
accion = ''
pendiente = 0
cobrado = 0
while accion != 'T':
    if accion == 'A':
        clave = input("Introduce el Numero de la Factura:")
        costo = float(input("Introduce el costo de la factura:"))
        facturas[clave] = costo
        pendiente += costo  # todo acumular todos los precios de las facturas
    if accion == "P":
        clave = input("Introduce el Numero de la factura a pagar:")
        costo = facturas.pop(clave, 0)
        cobrado += costo
        pendiente -= costo  # todo restando las factuas que ya estan pagadas
    print('Recaudado', cobrado)
    print('Pendiente de Cobro', pendiente)
    accion = input("Quieres añadir una nueva Factura(A) ,Pagarla(P) o Terminar(T)")
