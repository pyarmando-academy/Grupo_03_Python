class Hotel:
    def __init__(self, dire, nombre):
        self.nombre = nombre
        self.direccion = dire
        self.cuarto1 = Cuarto('101', 'Suite', '2 Personas', 500, '(D)')
        self.cuarto2 = Cuarto('201', 'Normal', '2 Personas', 150, '(M)')
        self.cuarto3 = Cuarto('301', 'Suite', '2 Personas', 2000, '(D)')
        self.cuarto4 = Cuarto('401', 'Premium', '2 Personas', 4500, '(D)')
        self.cuarto5 = Cuarto('601', 'Matrimonial', '2 Personas', 1500, '(D)')
        self.cuartos = {}

    def __str__(self):
        msj = f'Bienvenido a tu Hotel Favorito {self.nombre}'
        return msj

    def cargainicial(self):
        for cuarto in (self.cuarto1, self.cuarto2, self.cuarto3, self.cuarto4, self.cuarto5):
            self.cuartos[cuarto.vertipo('1')] = cuarto.vertipo('2')
        return self.cuartos

    def disponibilidad_cuartos(self):
        return self.cuartos

    def reservarcuartos(self):
        cuarto = input("Ingrese el Numero de cuarto a Reservar:")
        if cuarto in self.cuartos:
            self.cuartos[cuarto] = '(R)'
            print("Cuarto Reservado con exito")
        else:
            print("No Existe el Cuarto")


class Cuarto:
    def __init__(self, num, ti, cap, pre, flag):
        self.numero = num
        self.tipo = ti
        self.capacidad = cap
        self.precio = pre
        self.estado = flag

    def vertipo(self, campo):
        if campo == '1':
            return self.numero
        else:
            return self.estado


BuenaVista = Hotel("Jiron Medellin 234", "Buenavista")
print(BuenaVista)
BuenaVista.cargainicial()
print(BuenaVista.disponibilidad_cuartos())
BuenaVista.reservarcuartos()
print(BuenaVista.disponibilidad_cuartos())

"""
Funcionalidades
===============
1.-Hacer Varias Reservas a la vez
2.-No Permitir Reservar un cuarto que no  exista o que ya este ocupado
3.-Desarrollar el Metodo que me permita desocupar el Cuarto
4.-Una Vez que el cuarto este desocupado mostrar la tarifa que deberia pagar
5.-Realizar Un menu que cumpla con todas esas funcionalidades
7.-Realizar el proceso que los datos persistan "Crear Una Base de datos"
"""
