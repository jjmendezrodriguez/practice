<<<<<<< HEAD
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Robot:
    def __init__(self, id):
        self.id = id

    def identificar(self):
        return f"Soy un robot con ID {self.id}"

class PerroRobot(Perro, Robot):
    def __init__(self, nombre, edad, raza, id):
        Perro.__init__(self, nombre, edad, raza)
        Robot.__init__(self, id)

    def hacer_sonido(self):
        return "Guau robotizado"

    def identificar(self):
        return f"Soy un perro robot. Mi nombre es {self.nombre} y mi ID es {self.id}"

# Creación de instancias
animal = Animal("Animal genérico", 5)
perro = Perro("Rex", 3, "Labrador")
gato = Gato("Misu", 2)
perro_robot = PerroRobot("Cyborg", 4, "Ciber-Labrador", 101)

# Uso de métodos y propiedades
print(f"El perro {perro.nombre} dice: {perro.hacer_sonido()}")
print(f"El gato {gato.nombre} dice: {gato.hacer_sonido()}")
print(perro_robot.identificar())
print(f"El perro robot {perro_robot.nombre} dice: {perro_robot.hacer_sonido()}")
=======
a = [4,5,6]
b = [1,2,3]
c = b + a
print(c)

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list[2] = 2

print(my_list)
>>>>>>> 7f6014859859320bf503194a97678eef1430a965
