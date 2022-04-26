import csv


def suma(a, b):
    res = a + b
    return res


def cargar_empleados():
    with open('empleados_data.csv', 'r') as data:
        csv_leer = csv.reader(data)
        lista_empleados = list(csv_leer)
        return lista_empleados


def empleados_area(data, area_laboral):
    empleados_area = list()
    for codigo, empleado, año_nac, sueldo, area in data:
        if area == area_laboral:
            empleados_area.append((empleado, area))
    return empleados_area


def empleados_sueldo_area(data, area_laboral):
    tot_sueldo = 0
    for codigo, empleado, año_nac, sueldo, area in data:
        if area == area_laboral:
            tot_sueldo = tot_sueldo + float(sueldo)
    return tot_sueldo
