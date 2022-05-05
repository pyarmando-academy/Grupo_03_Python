"""
Escribir un programa que almacene las asignaturas de un ciclo
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura
 y elimine de la lista las asignaturas aprobadas. Al final el programa
 debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

cursos = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
aprobados = []
for curso in cursos:
    nota = float(input("Ingrese la nota del curso" + curso + "?:"))
    if nota >= 11:
        aprobados.append(curso)
for curso in aprobados:
    cursos.remove(curso)
print("Tienes que repetir" + str(cursos))
