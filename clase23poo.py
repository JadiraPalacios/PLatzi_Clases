class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

# Crear objetos de la clase Persona
persona1 = Persona("Jadira", 19)
persona2 = Persona("Trilce", 19)

persona1.saludar()
persona2.saludar()