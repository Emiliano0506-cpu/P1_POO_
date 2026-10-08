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
