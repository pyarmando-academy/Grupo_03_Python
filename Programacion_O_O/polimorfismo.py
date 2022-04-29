class Gato:
    def ruido(self):
        print('Gato Ruidoso')


class Perro:
    def ruido(self):
        print("Perror Ruidoso")


class Humano:
    def ruido(self):
        print('Humano Ruidoso')


def emitirruido(objetoType):
    objetoType.ruido()


Objgato = Gato()
Objperro = Perro()
ObjHumano = Humano()

emitirruido(ObjHumano)
