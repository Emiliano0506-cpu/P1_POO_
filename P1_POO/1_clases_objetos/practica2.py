"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class coches:
    def __init__(self,color,marca,velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad


    def acelerar(self):
        pass

    def frenar(self):
        pass

    def tocar_claxon(self):
        pass


#Instanciar o crear objetos de la clase Coches
coches1=coches('blanco','V2','220')
coches2=coches('azul','Nissan','180')

print(f"El color del coche es: {coches1.__color}")





