#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import coches

coche1 = coches("Toyota", "Corolla", 2020)
coche2 = coches("Honda", "Civic", 2021)

coche1.acelerar()
coche1.acelerar()

#print(coche1.__velocidad)
print(coche1.getVelocidad())
#coche1.__velocidad=400
coche1.setVelocidad(400)
#print(coche1.__velocidad)
print(coche1.getVelocidad())
class coches:
    pass

    # Marca
    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    # Color
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    # Modelo
    def getModelo(self):
        return self.__modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    # Velocidad
    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    # Potencia
    def getPotencia(self):
        return self.__potencia

    def setPotencia(self, potencia):
        self.__potencia = potencia

    # Asientos
    def getAsientos(self):
        return self.__asientos

    def setAsientos(self, asientos):
        self.__asientos = asientos

   