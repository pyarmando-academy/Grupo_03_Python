from utils import calculadora, calcular_edad

# print(calculadora(12, 5, "?"))

nombre = input("Ingrese el Nombre de la persona:")
año_nac = int(input("Ingrese el año de Nacimiento:"))
edad = calcular_edad(2022, año_nac)
print(f'{nombre} tiene de edad {edad}')
