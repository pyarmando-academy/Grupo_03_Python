'''

Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que
sea más fácil disponer la condición que verifica que es una vocal.
'''

# todo  hola mundo
cadena = input("Ingrese una oracion:")
cadena_min = cadena.lower()
vocales = "aeiou"
long_cad = len(cadena)
cant_voc = 0
for i in range(0, long_cad):
    if cadena_min[i] in vocales:
        cant_voc += 1

print("La Oracion ingresada es", cadena)
print("La Cantidad de Vocales", cant_voc)
