# Classes

# Definición

class MyEmptyPerson:
    pass # Para poder dejar la clase vacia

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y publicas

class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name # Propiedad privada
    
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Santiago", "Rivera")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Santiago", "Rivera", "Sinsinati")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Xavier de Lopez (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 555
print(my_other_person.full_name)