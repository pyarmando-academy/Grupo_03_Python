import datetime
import csv
import math
import statistics

import random
from random import randrange
from utils import suma

empleado = "Armando Ruiz"  # str
edad = 43  # int
estado = True  # bool
pago_hora = 23.8  # float
numero_azar = random.randrange(12, 67)

empleado = 1200

"""
precio = float(input("Ingrese el precio del producto:"))
cant = int(input("Ingrese la cantidad del producto:"))
cliente = input("Ingrese el nombre del cliente:")
total = precio * cant
# print("El Pago por su consumo es:" + str(total))
# print(f'El Cliente {cliente} Su total a pagar {total}:')
"""

"""
tipo = int(input("Tipo de Enfermedad:"))
edad = int(input("Ingrese la Edad del paciente:"))
dias = int(input("Numero estimado de dias:"))

if tipo == 1:
    costo_diario = 3150
elif tipo == 2:
    costo_diario = 3980
elif tipo == 3:
    costo_diario = 5500
elif tipo == 4:
    costo_diario = 7150
else:
    costo_diario = 0
if costo_diario == 0:
    print("\n El Tipo de Enfermedad no existe:")
else:
    costo_internacion = costo_diario * dias
    if edad < 18:
        costo_internacion *= 1.08
    elif edad > 70:
        costo_internacion *= 1.17
    print(f'\n Costo estimado a pagar:${costo_internacion:.2f}')
"""

codigo = input("Ingrese codigo del empleado:")
categoria = int(input("Ingrese El Grado Academico:"))
antiguedad = int(input("Ingrese Antiguedad:"))
respuesta = False
if categoria == 3 or categoria == 5:
    if antiguedad >= 5:
        respuesta = True
elif categoria == 1 or categoria == 2 or categoria == 4 and antiguedad >= 10:
    respuesta = True
if respuesta:
    resultado = 'Reune las caracteristicas para el puesto debe dar el test en el siguiente Link'
else:
    resultado = 'No Reune las caracteristicas para el puesto'
print(f'\n El Empleado con codigo {codigo} su Resultado es {resultado}')
