import random

# promedios = [23, 56, 13, 56, 78, 12, 56, 20]
#
# con = 0
# con2 = 0
# for item in promedios:
#     if item > 78:
#         con += 1
#     else:
#         con2 += 1
# print(f'EL Valor de con1 {con} y con2 {con2}')

# for x in range(10):
#     print("hola", x)

# edad = 0
# while edad < 18:  # True
#     edad = edad + 1
#     print(edad)


"""
passw = "python"
cont = 0

usuario = input("Ingrese el Nombre del Usuario:")
while True:
    con = input("Ingrese la Contraseña:")
    if con == passw:
        print(f'Bienvenido al Sistema {usuario}')
        break  # False
    else:
        print("Contraseña Errada")
        cont += 1
        if cont == 3:
            print("Supero Los Intentos, Vuelva a intentarlo en 24 Horas")
            break
        else:
            print(f'Intentos {cont}')
            
"""

numero_azar = random.randint(1, 100)
while True:
    numero = int(input("Cual es el numero que genero el compuador:"))
    if numero == numero_azar:
        print("Acertastes")
        break
    else:
        print("No Adivino el Numero")
