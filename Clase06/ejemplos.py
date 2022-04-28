# print("Ingrese las Tres Noras del Alumno")
# estu = input("Ingrese e Nombre del Estudiante:")
# n1 = int(input("Ingrese la Nota1:"))
# n2 = int(input("Ingrese la Nota2:"))
# n3 = int(input("Ingrese la Nota3:"))
# promedio = (n1 + n2 + n3) / 3
# if promedio > 10.5:
#     print(f'El Promedio obtenido por el estudiante {estu} es Aprobado')
# else:
#     print(f'El Promedio obtenido por el estudiante {estu} es Desaprobado')

estu = input("Ingrese el Nombre del estudiante:")
rc = int(input("Ingrese numero de respuestas correctas:"))
ri = int(input("Ingrese numero de respuestas incorrectas:"))
rb = int(input("Ingrese numero de respuestas en blanco:"))
prc = rc * 3
pri = ri * -1
prb = rb * 0
pf = prc + pri + prb
print(f'EL Estudiante {estu} su puntaje obtenido es de {pf}')
