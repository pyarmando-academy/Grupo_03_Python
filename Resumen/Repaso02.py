'''
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
ingresaron. Tener en cuenta que un espacio en blanco es igual a " ",
en cambio una cadena vacía es ""
'''

cadena = input("Ingrese una oracion:")
long_cad = len(cadena)
espacios = 0

for i in range(0, long_cad):
    if cadena[i] == " ":
        espacios += 1

print("La Cantidad de espacios en blanco es ", espacios)
