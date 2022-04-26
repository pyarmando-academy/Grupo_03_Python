# todo nucleo de python
import math
import random
import statistics

# print(math.pi)
# print(math.sqrt(4))
# print(math.cos(math.pi/4))

# print(random.randrange(1, 100))
# personas = ["Armando", "Ramon", "Arturo"]
# print(random.choice(personas))

datos = [2.90, 10.5, 14.7, 23.7, 10.5]
# print(statistics.mean(datos))
# print(statistics.median(datos))
# print(statistics.variance(datos))
# print(statistics.mode(datos))

from datetime import date

hoy = date.today()
# print(hoy)
# print(hoy.year)
# print(hoy.month)
# print(hoy.day)

empleado = input("Ingrese el nombre del empledo:")
fecha_nac = int(input("Ingrese su año de nacimiento:"))
año_actual = hoy.year

edad = int(año_actual) - fecha_nac
print(f'El empleado {empleado} tiene actualmente {edad} años')






