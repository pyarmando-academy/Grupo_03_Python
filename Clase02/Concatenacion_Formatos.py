mentor = "Armando"
curso = "Python"
alumnos = 20
tiempo = 7.8

# print(mentor + curso + str(alumnos))
# print(mentor, curso, alumnos)
# print("%s tiene %d alumnos y el tiempo es %.1f" % (mentor, alumnos, tiempo))
# print ("{} tiene {} alumnos y el tiempo es {}".format(mentor,alumnos,tiempo))
# print(f'{mentor} tiene {alumnos}  alumnos y el tiempo es {tiempo}')


# todo entrada
pago_hora = 60.00
nom_emp = input("Ingrese el nombre del empleado:")
horas_trab = int(input("Ingrese las horas trabajadas:"))
# todo proceso
pago_jornal = horas_trab * pago_hora
# todo salida
print(f"El Empleado {nom_emp} su pago diario es  S/.{pago_jornal}")



