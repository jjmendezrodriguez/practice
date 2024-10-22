#!/bin/python

class Autos:
    def __init__(self, marca: str, modelo, color, miles):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.miles = miles
        
    def stats(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Color: " + self.color)
        print("Miles: " + str(self.miles))
        # print(self)

    def to_dict(self):
        return self.__dict__
        
        
# Pedro_car = Autos('Toyota', 'Corolla', 'black', 83000)
# Jose_car = Autos('Toyota', 'Corolla', 'black', 83000)

# Pedro_car.stats()
# print("\n\n---\n\n")
# Jose_car.stats()