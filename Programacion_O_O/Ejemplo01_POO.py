class Animal():
    # Constructor
    # todo definiendo los Atributos
    def __init__(self, nombre, edad, pelaje="blanco"):
        self.nombre = nombre
        self.edad = edad
        self.pelaje = pelaje

    # todo creando los metodos
    def __str__(self):
        dato = f'El Animal con nombre {self.nombre} tiene {self.edad} de edad'
        return dato

    def msj_edad(self):
        if self.edad >= "1" and self.edad <= "2":
            msj = "La Mascota es Cachorra"
        else:
            msj = "La Mascota es Adulta"
        return msj


perro = Animal("Pancho", "4 Años")
gato = Animal("Paco", "1 Año", "rubio")

print(perro.msj_edad())
print(gato.msj_edad())

# print(perro.__dict__)
# print(gato.__dict__)

# print(perro)

# print(perro.edad)
# print(perro.nombre)
# print(perro.pelaje)
#
# print(gato.nombre)
# print(gato.pelaje)

# print(perro)
# print(gato)
