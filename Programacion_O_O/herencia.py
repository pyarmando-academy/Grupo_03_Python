# todo clase Base1

class Telefono:
    def __init__(self, numero):
        self.numero = numero

    def llamar(self):
        print("Te Estoy Lamando")

    def colgar(self):
        print("Me Canse de Llamarte")

    def __str__(self):
        return self.numero


# todo clase Base2
class Camara:
    def __init__(self, mpx):
        self.mpx = mpx

    def fotografiar(self):
        print("Te quiero tomar un Selfee")

    def __str__(self):
        return self.mpx


# todo clase Base3

class Reproductor:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def reproducirvideo(self):
        print("Estoy Viendo mi clase de PYTHON Favorita")

    def reproducirsonido(self):
        print("Estoy Escuchando las clases de PYTHON")

    def __str__(self):
        return self.capacidad


# clase Hija

class Movil(Telefono, Camara, Reproductor):
    def __init__(self, numero, mpx, capacidad):
        Telefono.__init__(self, numero)
        Camara.__init__(self, mpx)
        Reproductor.__init__(self, capacidad)

    def __str__(self):
        return "Numero {0} , Camara{1}, Capacidad{2}".format(Telefono.__str__(self), Camara.__str__(self),
                                                             Reproductor.__str__(self))


android = Movil('9456788', '500px', '1Giga')
print(android)
