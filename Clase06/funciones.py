def test():
    print("Esto es una funcion")


def saludar(nombre):
    return f'Hola {nombre} Bienvenido al curso de PYTHON'


def mensaje(nombre, mensaje="Adios"):
    saludo = mensaje, nombre
    return saludo


def saluda(*nombres):
    for nom in nombres:
        print(nom)


nombres = ["Juan", "Pedro", "Maria"]

saluda(nombres)
# for nom in nombres:
#     print(nom)

# print(saludar("armando"))
# print(mensaje("Armando", "Hola"))
