### Classes ###

class MyEmptyPerson:  #Los nombres de las clases se definen con CamelCase
    pass

print(MyEmptyPerson)
print(MyEmptyPerson)

# Creación de un constructor

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # Propiedad privada
        self.__surname = surname # Propiedad pública
        
 # Podemos crear setter and getter
        
    def get_name(self):
        return self.__name
        
    def walk(self): # Se le debe pasar el parámetro self
        print(f"{self.full_name} está caminando")
    
my_person = Person("Luis", "Gordon")
print(my_person.get_name())
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Luis", "Gordon", "Luka")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
my_other_person.walk()