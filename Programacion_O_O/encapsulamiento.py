class Factura:
    __igv = 18

    def __init__(self, unidad, precio, ):
        self.unidad = unidad
        self.precio = precio

    def atributo_igv(self):
        return self.__igv

    def porpagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura.__igv / 100
        return total + impuesto


compra = Factura(5, 1200)
print(compra.atributo_igv())
print(compra.porpagar())
